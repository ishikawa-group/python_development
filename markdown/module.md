# Directory trees in Python library
* Following is the typical directory trees in Python library.
```
mypackage/
 ├── mypackage/
 │   ├── __init__.py
 │   ├── module1.py
 │   `── module2.py
 │
 ├── tests/
 │   ├── test_module1.py
 │   `── test_module2.py
 │
 ├── setup.py
 ├── README.md
 `── requirements.txt
```

* In the above case, calling `mod.py` from test.py is done as:
  ```python
  from sub_project import mod
  ```
* You need to distinguish "library" and "application".
  + Library: Codes used by import
  + Application: Directory execured.
  + If you want to use a script in both library and application purposes, name it as `__main__.py`.
    * In that case, execute as `python -m (project)`.
