# membership

[![GitHub Repo stars](https://img.shields.io/github/stars/AmanoShizukikun/membership?style=social)](https://github.com/AmanoShizukikun/membership/stargazers)
[![GitHub last commit](https://img.shields.io/github/last-commit/AmanoShizukikun/membership)](https://github.com/AmanoShizukikun/membership/commits/main)
[![GitHub release](https://img.shields.io/github/v/release/AmanoShizukikun/membership)](https://github.com/AmanoShizukikun/membership/releases)

\[ 中文 | [English](https://github.com/AmanoShizukikun/membership/blob/main/assets/docs/README_en.md) | [日本語](https://github.com/AmanoShizukikun/membership/blob/main/assets/docs/README_jp.md) \]

## 簡介
勤益科技大學 Web 程式設計第3次回家作業。

## 近期變動
###  1.0.0 (2025 年 5 月 23 日)
![t2i](https://github.com/AmanoShizukikun/membership/blob/main/assets/preview/1.0.0.jpg)
### 重要變更
- 【重大】首個發行版本。
### 新增功能
- N/A
### 已知問題
- N/A

[所有發行版本](https://github.com/AmanoShizukikun/membership/blob/main/assets/docs/Changelog.md)

## 快速開始
> [!NOTE]
> 此為必要步驟。
### 環境設置
- **Python 3**
  - 下載: https://www.python.org/downloads/windows/
- **SQLite**
  - 下載: https://sqlite.org/download.html

### 安裝倉庫
> [!IMPORTANT]
> 此為必要步驟。
```shell
git clone https://github.com/AmanoShizukikun/membership.git
cd membership
pip install -r requirements.txt
```

### 開啟網頁
```shell
flask --debug run
```

## 待辦事項
- **高優先度：**
  - [x] 快速安裝指南。
  - [ ] 使用指南(wiki)。

- **功能:**
  - 資料庫
    - [x] 程式第一次啟動時，建立 membership.db 與 members 資料表並新增記錄。
    
  - 程式
    - [x] 首頁。
    - [x] 註冊頁面。
    - [x] 登入頁面。
    - [x] 修改基本資料頁面。 
    - [x] 刪除用戶功能。
    - [x] 錯誤頁面。
    - [x] 樣板繼承。
    - [x] CSS 樣式。

## 致謝
特別感謝以下項目和貢獻者：

### 項目
N/A

### 貢獻者
<a href="https://github.com/AmanoShizukikun/membership/graphs/contributors" target="_blank">
  <img src="https://contrib.rocks/image?repo=AmanoShizukikun/membership" />
</a>
