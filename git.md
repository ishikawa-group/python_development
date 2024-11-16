# Git
## Github Flow
* ブランチの運用に関するルールを定めたもの
  + main: 公開するブランチ
  + develop: 開発用ブランチ
  + feature: 機能の開発など。適宜わかりやすいブランチ名にする
  + featureについては自由にpushしてよく、機能が固まったらdevelopにpull requestする
  + featureからmainへのpull requestは管理者が行う
* feature -> developおよびdevelop -> mainへのpull requestの際にはGithub Actionsにより自動テストを行う(後述)

## pull request
* コードを作成したブランチを他のブランチにまとめる(merge)すること
* 大抵は管理者に確認(review)してもらい、承認してもらったらpull requestが完了する

### 手順
* 以下、"feature"ブランチを作成し、"develop"にpull requestする
0. オリジナルのレポジトリをcloneする
  * `git clone https://github... .`
1. 作業用ブランチを作る("feature")
  * `git checkout -b feature`
2. ファイルを編集
  * `vi ...`
3. 編集ファイルをadd, commitする
  * `git add .`
  * `git commit -m "made some change"`
4. featureブランチからGithub上のoriginブランチにpushする
  * 初回のみ: `git push --set-upstream origin feature`
  * 2回目以降: `git push`
5. Github上(ブラウザ)で該当するレポジトリにアクセス、Pull requestを行う
  * 緑の"Compare & Pull request"をクリックする
  * "base"が*マージ先*で"compare"が*マージ元*になっていることを確認
  * 上記のタブがなければブランチの選択で"feature"を選んで"Contribute", "Open pull request"をクリック
6. "Create pull request"をクリック
  * コメントなどの情報を入れる
  * コードの差分などを確認
7. ブランチをマージする
  * 管理者が行う
  * pull requestを承認する場合は"Confirm merge"
  * 承認しない場合は"Close pull request"する
  * 一度承認してしまって、やっぱり元に戻したい場合は"revert"をクリックする
  * Github Actionsでpull requestに伴うチェックが入る場合は、この段階で入る
    + チェックを通過しなければfailedになる
    + failしてもマージすることは可能

* mainが更新されたらdevelopなど、他のbranchも更新すること
  + ブラウザでdevelopなどに移動し、"This branch is X commits behind main"をクリック -> pull requestでマージする

# Github Actions
* Githubが提供しているCI/CDツール
* テストやフォーマッティングなどを自動化できる

## 利用法
* フローで行いたい処理を書いたYAMLファイルを`./github/workflow/`に置く
* YAMLファイルに書かれたイベント(push, pull requestなど)が行われたら自動的に処理が行われる
* 処理の結果などの詳細はGithub(ブラウザ)で確認する
* YAMLのテンプレートは https://github.com/marketplace?type=actions にある

## Hello world
```yaml
name: Hello world
on: push

jobs:
  build:
    name: Greeting
    runs-on: ubuntu-latest
    steps:
      - run: echo "Hello world"
```
* on:に動くきっかけを記載します。
  + 今回は、pushのタイミングで動かしたかったのでpushと書きました
* runs-on:に実行環境を記載します
  + 今回は、最新のUbuntu環境で動かしたかったのでubuntu-latestと書きました
* steps:に実行したい内容を書きます
  + 今回は、画面にHello World!を表示させたいのでechoを書きました

## フォーマットチェック
```yaml
name: formatting check with flake8

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  command:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: 3.11

      - name: Install dependencies
        run: pip install flake8
      - name: Run checking
        run: flake8 .
```
## 設定の意味
* jobs
  + 処理の最上位単位です。jobsの中に1つ以上のジョブIDと共に処理が設定され、並列で実行されます
* on
  + どのイベントが発生したら処理を実行するか指定します
* runs-on
  + ジョブを実行するOS(ランナー)を指定します
* uses
  + 第三者もしくはGitHubが作成したActionsをyml内に記載することで実行することもできます。よく使われているのがGitHubが用意しているactions/checkout@v4です
* steps
  + jobsは1つ以上のstepsで構成されており、stepsの中にrunコマンドが1つ以上構成されています
* run
  + runに実行するコマンドを以下のように記載していきます。nameにrunの処理について書くことができ、GitHub上で確認できます