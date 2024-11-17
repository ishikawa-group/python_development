# Honkit
* Honkitは、GitBookのフォークであり、静的サイトジェネレーターとして使用される
* GitBookは有料で登録が必要なのでこちらの方が楽?

# 使い方
1. Honkitのインストール
* まず、Node.jsがインストールされていることを確認してください。その後、以下のコマンドを実行してHonkitをインストールする
```bash
npm install honkit --save-dev
```

2. プロジェクトのセットアップ
* 新しいプロジェクトディレクトリを作成し、その中に移動
```bash
mkdir mybook
cd mybook
```

3. 初期設定ファイルの作成
* Honkitの初期設定ファイルを作成する
```bash
npx honkit init
```
* このコマンドを実行すると、README.mdとSUMMARY.mdという2つのファイルが生成される
    + README.md: 本の紹介や概要を書くファイル
    + SUMMARY.md: 本の目次を定義するファイル

4. 本の内容を追加
* README.mdとSUMMARY.mdを編集して、本の内容を追加する
* 例えばSUMMARY.mdは以下のようになる
    + フォルダを分けない場合
    ```markdown
    # Summary
    * [Introduction](README.md)
    * [Part1](part1.md)
    * [Part2](part2.md)
    ```
    + フォルダを分ける場合
    ```markdown
    # Summary
    * [Introduction](README.md)
    * [Chapter 1](chapter1/README.md)
        * [Contents of Chapter 1](chapter1/contents.md)
    * [Chapter 2](chapter2.md)
        * [Contents of Chapter 2](chapter2/contents.md)
  ```

5. ローカルサーバーでプレビュー
* 以下のコマンドを実行して、ローカルサーバーで本をプレビューする
```bash
npx honkit serve
```
* ブラウザで http://localhost:4000 にアクセスすると本の内容を確認できる

# プラグインのインストール
* https://www.npmjs.com/ から検索するとよい
* インストールコマンドも同時に表示されるのでそれを使う
* honkit用とgitbook用がある。どちらで動くかはあまりよくわからない。

# book.jsonの設定
* htmlの設定は`book.json`で設定する

## コードハイライト
* ハイライトを変えたい場合はprismなどを使う: `{"plugins": ["prism", "-highlight"]}`

## "Honkitで公開"の削除
* サイドバーにあるHonkitで公開 (Published with Honkit)を削除: `{"plugins": ["hide-published-with"]}`

## 数式
* mathjax: `{"plugins": ["mathjax"]}`
* katex: `{"plugins": ["katex"]}`
* katex + mhchem: `{"plugins: ["katex-mhchem"]}`

# webで公開
1. プロジェクトの初期化
* ローカルでプロジェクトディレクトリを作成し、Gitリポジトリを初期化する
```bash
mkdir mybook
cd mybook
git init
```

2. Honkitプロジェクトのセットアップ
* Honkitプロジェクトをセットアップし、HTMLをビルドする
```bash
honkit init
honkit build . docs
```

3. ファイルをコミット
* すべてのファイルをGitに追加し、コミットする
```bash
git add .
git commit -m "Initial commit"
```

4. リモートリポジトリにプッシュ
* リモートリポジトリを追加し、ローカルの変更をプッシュする
```bash
git remote add origin https://github.com/your_name/mybook.git
git push -u origin main
```

5. GitHub Pagesの設定
* GitHubリポジトリの設定ページに移動し、GitHub Pagesのセクションを見つける
* "Source"を"main"の"/docs"ディレクトリに設定する

6. 公開URLの確認
* 設定が完了すると、GitHub PagesのURLが表示される
* このURLにアクセスすると、docsディレクトリ内のHTMLが公開されていることを確認できる
* "About"のWebsiteにGitHub PagesのURLを使うとよい
