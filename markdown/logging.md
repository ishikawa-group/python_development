# logging
* `logging` is a library for outputting logs.
* While it's fine to start with `print` for Python script output, it's better to use `logging` when possible.
1. Flexibility: Logging allows you to set different logging levels (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL) and control the output based on the level of importance.
2. Configurability: Logging can be configured to output messages to different destinations, such as the console, files, or external systems, without changing the code.

## Basic log output
```python
import logging

logging.basicConfig(level=logging.INFO)

logging.debug("Debug log")  # Not displayed (INFO and above only)
logging.info("Information log")
logging.warning("Warning log")
logging.error("Error log")
logging.critical("Critical error log")
```
**Output result**
```
INFO:root:Information log
WARNING:root:Warning log
ERROR:root:Error log
CRITICAL:root:Critical error log
```

## Save logs to file
```python
logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logging.info("Log recorded to file")
```
* Logs are saved to `app.log`.

## Output to both console & file
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

logger.info("Output to console and file")
```
* Logs are recorded to **both console & file**.
