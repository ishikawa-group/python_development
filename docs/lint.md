# Lint
* "静的解析"を行うツール一般のこと。静的解析は、コードのフォーマットなどがあっているかどうかを確認する
* コードにエラーがなくて実行が可能であっても、フォーマットなどがメチャクチャだと読みにくい。そこで、Pythonコードがルールに合っているかどうかをチェックする
* Pythonコードのフォーマットは*PEP8*と呼ばれるルールがあり、それに従うように書かれることが多い
* Pythonであれば、このLintの部分には`flake8`や`black`というライブラリが用いられる -> ここでは`flake8`を使う

## flake8
* PythonファイルがPEP8に適合しているかどうかチェックする
* エラーメッセージを出すのみで**上書きはしない**
* インストール: `pip install flake8`
* 実行
  + `flake8 .`: 全てのファイル
  + `flake8 main.py`: main.pyのみチェック
* なお、flake8自体は下記ライブラリのラッパー
  1. PyFlakes（pyflakes : コードのエラーチェック）
  2. pycodestyle（pycodestyle : PEP8に準拠しているかチェック）
  3. Ned Batchelder’s McCabe script（mccabe : 循環的複雑度のチェック）

### オプション
* `--ignore`: このオプションをつけることで、特定のerrorを無視します:
  ```
  flake8 --ignore E402
  flake8 main.py --ignore E402,E403
  ```
* `--max-line-length`: このオプションをつけることで、1行あたりの最大文字数を指定する
  ```
  flake8 --max-line-length 100
  ```
* 個人的に使う設定: `flake8 . --max-line-length 120 --ignore E201,E221,E225,E226,E241,W605`

## isort
* Pythonファイルのimport部分をフォーマットする
* ファイルを**上書きする**
* インストール: `pip install isort`

### オプション
* `--no-sections`: 標準ライブラリ、自作ライブラリなどのセクションに分けない
* `--force-single-line-imports`: 1行につきimport1つに強制する
* 個人的に使う設定： `isort main.py --no-sections --force-single-line-imports`
