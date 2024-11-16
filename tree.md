# Directory trees in Python library
* Following is the typical directory trees in Python library.
```
(project)
|-- (project) ... Source directory for scripts
|   |-- __init__.py
|   `-- *.py
|
|-- (sub_project)
|   |-- __init__.py
|   `-- *.py
|
|-- tests ... Test scripts
    |-- __init__.py
    `-- *.py
```
* When the Python script is only one, you can put test codes in `project`.
* In the above case, calling `mod.py` in (sub_project) is done as:
    ```python
    from sub_project import mod
    ```
* You need to distinguish "library" and "application".
  + Library: Codes used by import
  + Application: Directory execured.
  + If you want to use a script in both library and application purposes, name it as `__main__.py`.
    * In that case, execute as `python -m (project)`.