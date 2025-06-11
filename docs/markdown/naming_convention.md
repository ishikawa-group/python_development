# Python Library Naming Conventions

| Element                             | Naming Style    | Example             | Notes                                            |
| ----------------------------------- | --------------- | ------------------- | ------------------------------------------------ |
| **GitHub Repository Name**          | `kebab-case`    | `my-library`        | For URL readability. Lowercase is recommended.  |
| **Import Name** (`import x`)        | `snake_case`    | `import my_library` | Should match `src/`.                             |
| **Directory under `src/`**          | `snake_case`    | `src/my_library/`   | Acts as the top-level. Should match import name. |
| **Module Name** (`.py` filename)    | `snake_case.py` | `data_loader.py`    | Submodule name is `my_library.data_loader`.      |
| **Project Name (`pyproject.toml`)** | `kebab-case`    | `my-library`        | Used in PyPI & `pip install`.                    |
| **File Name**                       | `snake_case.py` | `train_model.py`    | Should be descriptive.                           |
| **Class Name**                      | `CamelCase`     | `ImageClassifier`   | Capitalize each word.                            |
| **Function Name**                   | `snake_case()`  | `train_model()`     | Describes an action.                             |
| **Variable Name**                   | `snake_case`    | `learning_rate`     | Clear and concise.                               |
| **Constant Name**                   | `UPPER_CASE`    | `MAX_EPOCHS`        | Used for module-level constants.                 |

## Key Recommendations

- Use `src/` layout: place your main package under `src/<import_name>/`.
- Prefer consistency across PyPI name, import name, and repository name when possible.
- Use `kebab-case` for GitHub and PyPI if allowed; `snake_case` for all Python identifiers.
- Avoid hyphens (`-`) in anything that is used in `import` statements — they will cause syntax errors.

## Example Layout
```
my-library/
├── src/
│   └── my_library/           # ← import my_library
│       ├── init.py
│       └── data_loader.py    # ← my_library.data_loader
├── pyproject.toml            # ← project.name = “my-library”
├── tests/
└── README.md
```