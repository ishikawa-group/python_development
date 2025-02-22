# logging
* ログ(履歴)を出力する
* Pythonスクリプトの出力は、最初は`print`でも良いが可能なら`logging`にしたほうがよい

## 基本のログ出力
```python
import logging

logging.basicConfig(level=logging.INFO)

logging.debug("デバッグログ")  # 表示されない（INFO以上が対象）
logging.info("情報ログ")
logging.warning("警告ログ")
logging.error("エラーログ")
logging.critical("致命的エラーログ")
```
**出力結果**
```
INFO:root:情報ログ
WARNING:root:警告ログ
ERROR:root:エラーログ
CRITICAL:root:致命的エラーログ
```

## ログをファイルに保存
```python
logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logging.info("ファイルに記録されるログ")
```
--> `app.log` にログが保存される。

## コンソール＆ファイル両方に出力
```python
logger = logging.getLogger("MyLogger")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("app.log")

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.info("コンソールとファイルに出力")
```
--> **コンソール＆ファイル** にログが記録される。