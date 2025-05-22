# membership

[![GitHub Repo stars](https://img.shields.io/github/stars/AmanoShizukikun/membership?style=social)](https://github.com/AmanoShizukikun/membership/stargazers)
[![GitHub last commit](https://img.shields.io/github/last-commit/AmanoShizukikun/membership)](https://github.com/AmanoShizukikun/membership/commits/main)
[![GitHub release](https://img.shields.io/github/v/release/AmanoShizukikun/membership)](https://github.com/AmanoShizukikun/membership/releases)

\[ [中文](https://github.com/AmanoShizukikun/membership/blob/main/README.md) | [English](https://github.com/AmanoShizukikun/membership/blob/main/assets/docs/README_en.md) | 日本語 \]

## 紹介
国立勤益科技大学 Webプログラミング 第3回宿題。

## 最近の変更
###  1.0.0 (2025年5月23日)
![t2i](https://github.com/AmanoShizukikun/membership/blob/main/assets/preview/1.0.0.jpg)
### 主要な変更
- 【重要】初回リリースバージョン。
### 新機能
- N/A
### 既知の問題
- N/A

[すべてのリリース](https://github.com/AmanoShizukikun/membership/blob/main/assets/docs/Changelog.md)

## クイックスタート
> [!NOTE]
> これらは必須ステップです。
### 環境設定
- **Python 3**
  - ダウンロード: https://www.python.org/downloads/windows/
- **SQLite**
  - ダウンロード: https://sqlite.org/download.html

### リポジトリのインストール
> [!IMPORTANT]
> このステップは必須です。
```shell
git clone https://github.com/AmanoShizukikun/membership.git
cd membership
pip install -r requirements.txt
```

### ウェブサイトの起動
```shell
flask --debug run
```

## ToDo リスト
- [ ] **高優先度：**
  - [x] クイックインストールガイド。
  - [ ] ユーザーガイド（wiki）。

- [ ] **機能:**
  - データベース
    - [x] プログラム初回起動時にmembership.dbとmembersテーブルを作成し、レコードを追加。
    
  - プログラム
    - [x] ホームページ。
    - [x] 登録ページ。
    - [x] ログインページ。
    - [x] プロフィール編集ページ。
    - [x] ユーザー削除機能。
    - [x] エラーページ。
    - [x] テンプレート継承。
    - [x] CSSスタイリング。

## 謝辞
以下のプロジェクトと貢献者に特別な感謝を表します：

### プロジェクト
N/A

### 貢献者
<a href="https://github.com/AmanoShizukikun/membership/graphs/contributors" target="_blank">
  <img src="https://contrib.rocks/image?repo=AmanoShizukikun/membership" />
</a>