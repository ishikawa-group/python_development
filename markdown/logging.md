# logging
* `logging` is a library for outputting logs.
* While it's OK to start with `print` for Python script output, it's better to use `logging` when possible, from following reasons:
1. Flexibility: Logging allows you to set different logging levels (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL) and control the output based on the level of importance.
2. Configurability: Logging can be configured to output messages to different destinations, such as the console, files, or external systems, without changing the code.

## Basic log output
* Following is the basic usage of logging.

```python
import logging

# only output the INFO level
logging.basicConfig(level=logging.INFO)

# choose one of the following log according to your purpose
logging.debug("Debug log")  # this is not displayed
logging.info("Information log")
logging.warning("Warning log")
logging.error("Error log")
logging.critical("Critical error log")
```

**Output result**
* In this above case, the logs are outputted to the standard output, as

```
INFO:root:Information log
WARNING:root:Warning log
ERROR:root:Error log
CRITICAL:root:Critical error log
```

* Datetime formatting can be specified by `datafmt`.

```python
logging.basicConfig(..., datefmt='%Y-%m-%d %H:%M:%S', ...)
```

## Save logs to file

```python
logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logging.info("Log recorded to file")
```

* Logs are saved to `app.log`.

## Save logs to both file and standard output

```python
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),  # Output to standard output
        logging.FileHandler("app.log", mode="w")  # Output to a file
    ]
)

# Example logs
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
```

---

## When you have main and other functions

### 1. Using Logging in `main` and Other Functions (Single File)
* Use `logging.getLogger(__name__)` in each function.
* Configure logging only once in `main()`.
* Use different log levels (`DEBUG`, `INFO`, etc.).
* Log to both console and a file.

#### Example

```python
import logging
import sys


def function_one():
    logger.debug("This is a debug message from function_one")


def function_two():
    logger.info("This is an info message from function_two")


if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler("app.log", mode="w")
        ]
    )

    # Create logger
    logger = logging.getLogger(__name__)

    logger.info("Starting application")
    function_one()
    function_two()
    logger.warning("Application is ending")
```

### 2. Using Logging in `main` and Other Functions (Multiple Files)
* Configure logging only in `main.py`.
* Each module (`utils.py`, etc.) should use `logging.getLogger(__name__)`.
* Logs from modules will automatically follow `main.py`'s configuration.
* Log messages will include module names, helping with debugging.

#### Project Structure:
```
/project
│── main.py      # Main script
│── utils.py     # Separate module
│── app.log      # Log file (generated at runtime)
```

#### `main.py` (Main Script)

```python
import logging
import sys
import utils  # Import the module

# Configure logging in main.py
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("app.log", mode="w")
    ]
)

logger = logging.getLogger(__name__)  # Logger for main.py

if __name__ == "__main__":
    logger.info("Starting application")
    utils.function_one()
    utils.function_two()
    logger.warning("Application is ending")
```

### `utils.py` (Module with Functions)
```python
import logging

logger = logging.getLogger(__name__)  # Logger for utils.py

def function_one():
    logger.debug("This is a debug message from function_one in utils.py")

def function_two():
    logger.info("This is an info message from function_two in utils.py")
```

### Summary
* **Single file:** Configure logging in `main()`, use `getLogger(__name__)` in functions.  
* **Multiple files:** Configure logging in `main.py`, and let modules (`utils.py`, etc.) inherit it.  
* Logs are formatted and stored in `app.log` while also appearing in the console.
