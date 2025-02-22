# Sphinx
* https://github.com/executablebooks/MyST-Parser

# ライブラリのインストール
## ローカルにあるパッケージのインストール
* `setup.py`のある場所に移動し`pip install --editable .`
* `editable`をつけておくと、コードの変更がライブラリを使った場合にも反映される
* `setup.py`は以下のようにすること
  ```python
  from setuptools import setup
  from setuptools import find_packages

  setup(
      name="パッケージ名",
      version="0.1.0",
      license="ライセンス",
      description="パッケージの説明",
      author="作成者",
      url="GitHubなどURL",
      packages=find_packages(include=["your_modules"]),
  )
  ```

## PyPI
* `pip install xxx`でインストールできるようにする

### testPyPIで試す
* `setup.py`を作る
* testPyPIのアカウントを作成
* tokenを作成
* `~/.pypirc`を作成。usernameを`__token__`にし、passwordにtokenをペースト
  * usernameをログイン名に、passwordをパスワードにしてもよいが平文なのがネック
* `python -m build`: --> `dist`ができる
* `python -m twine upload --repository testpypi dist/*`
* `pip install -i https://test.pypi.org/simple/ my_package_name`: これでインストールできる

* 同じversion番号だと複数回アップロードできないので注意
* サブディレクトリにもすべて`__init.py__`を入れること。中身は空で良い

#### refs
* https://packaging.python.org/en/latest/tutorials/packaging-projects/
* https://zenn.dev/sikkim/articles/490f4043230b5a

#### requirements.txtの自動作成
* pipreqsで簡単に作成できる
```python
pip install pipreqs
pipreqs .
```
