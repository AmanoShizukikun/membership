from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
import os

app = Flask(__name__)

DATABASE = 'membership.db'

def init_db():
    if not os.path.exists(DATABASE):
        with sqlite3.connect(DATABASE) as conn:
            c = conn.cursor()
            c.execute('''
                CREATE TABLE IF NOT EXISTS members (
                    iid INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    phone TEXT,
                    birthdate TEXT
                )
            ''')
            c.execute('''
                INSERT OR IGNORE INTO members (username, email, password, phone, birthdate)
                VALUES ('admin', 'admin@example.com', 'admin123', '0912345678', '1990-01-01')
            ''')
            conn.commit()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        birthdate = request.form['birthdate']
        if not username or not email or not password:
            return render_template('error.html', error_message='請輸入用戶名、電子郵件和密碼')

        with sqlite3.connect(DATABASE) as conn:
            c = conn.cursor()
            try:
                c.execute("SELECT 1 FROM members WHERE username = ?", (username,))
                if c.fetchone():
                    return render_template('error.html', error_message='用戶名已存在')
                c.execute("SELECT 1 FROM members WHERE email = ?", (email,))
                if c.fetchone():
                     return render_template('error.html', error_message='電子郵件已存在')
                c.execute("INSERT INTO members (username, email, password, phone, birthdate) VALUES (?, ?, ?, ?, ?)",
                          (username, email, password, phone, birthdate))
                conn.commit()
                return redirect(url_for('login'))
            except sqlite3.IntegrityError: 
                return render_template('error.html', error_message='註冊失敗，資料庫錯誤，請稍後再試')
            except Exception as e:
                return render_template('error.html', error_message=f'註冊過程中發生未知錯誤: {str(e)}')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if not email or not password:
            return render_template('login.html', error_message='請輸入電子郵件和密碼', email=email)

        with sqlite3.connect(DATABASE) as conn:
            c = conn.cursor()
            c.execute("SELECT iid, username FROM members WHERE email = ? AND password = ?", (email, password))
            user = c.fetchone()
            if user:
                iid, username = user
                return redirect(url_for('welcome', iid=iid))
            else:
                return render_template('login.html', error_message='電子郵件或密碼錯誤', email=email)

    return render_template('login.html')

@app.route('/welcome/<int:iid>') 
def welcome(iid):
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute("SELECT username FROM members WHERE iid = ?", (iid,))
        user_data = c.fetchone()
        if not user_data:
            return render_template('error.html', error_message='用戶不存在或無法載入歡迎頁面')
        username = user_data[0]     
    return render_template('welcome.html', username=username, iid=iid)


@app.route('/edit_profile/<int:iid>', methods=['GET', 'POST'])
def edit_profile(iid):
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute("SELECT username, email, phone, birthdate FROM members WHERE iid = ?", (iid,))
        user = c.fetchone()
        if not user and request.method == 'GET': 
            return render_template('error.html', error_message='用戶不存在')
        
    if request.method == 'POST':
        email_form = request.form['email']
        password_form = request.form['password']
        phone_form = request.form['phone']
        birthdate_form = request.form['birthdate']
        current_username_for_form = ""
        if user:
            current_username_for_form = user[0]
        else:
            with sqlite3.connect(DATABASE) as conn_check_user:
                c_check = conn_check_user.cursor()
                c_check.execute("SELECT username FROM members WHERE iid = ?", (iid,))
                user_for_form_check = c_check.fetchone()
                if user_for_form_check:
                    current_username_for_form = user_for_form_check[0]
                else: 
                    return render_template('error.html', error_message='用戶不存在，無法修改資料')
        if not email_form or not password_form:
            return render_template('edit_profile.html', error_message='請輸入電子郵件和密碼',
                                   username=current_username_for_form, 
                                   email=email_form,
                                   phone=phone_form,
                                   birthdate=birthdate_form,
                                   iid=iid)
        with sqlite3.connect(DATABASE) as conn_update:
            c_update = conn_update.cursor()
            c_update.execute("SELECT COUNT(*) FROM members WHERE email = ? AND iid != ?", (email_form, iid))
            if c_update.fetchone()[0] > 0:
                return render_template('error.html', error_message='電子郵件已被使用')
            
            c_update.execute("UPDATE members SET email = ?, password = ?, phone = ?, birthdate = ? WHERE iid = ?",
                             (email_form, password_form, phone_form, birthdate_form, iid))
            conn_update.commit()
            return redirect(url_for('welcome', iid=iid))
    if user:
        username, email_orig, phone_orig, birthdate_orig = user
        return render_template('edit_profile.html', username=username, email=email_orig, 
                               phone=phone_orig, birthdate=birthdate_orig, iid=iid)
    else:
        return render_template('error.html', error_message='無法載入使用者資料進行編輯')


@app.route('/delete/<int:iid>', methods=['GET', 'POST']) 
def delete(iid):
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute("DELETE FROM members WHERE iid = ?", (iid,))
        conn.commit()
    return redirect(url_for('index'))

@app.template_filter('add_stars')
def add_stars(s):
    return f'★{s}★'

if __name__ == '__main__':
    pass