
## Summary Table

| Item                      | Naming Style      | Example                    | Notes |
|---------------------------|-------------------|----------------------------|-------|
| **GitHub Repository Name**| `kebab-case`      | `my-library`               | Good for readability in URLs. Separate from the Python module name. |
| **Module Name**           | `snake_case`      | `my_library`               | Used in `import` statements. Hyphens (`-`) are not allowed. |
| **File Name (.py)**       | `snake_case.py`   | `data_loader.py`           | Should align with the module name. |
| **Class Name**            | `CamelCase`       | `MyModel`, `DataLoader`    | Capitalize each word. Also known as PascalCase. |
| **Function Name**         | `snake_case()`    | `train_model()`            | Should express an action. |
| **Variable Name**         | `snake_case`      | `learning_rate`, `count`   | Descriptive but concise. |
| **Constant Name**         | `UPPER_CASE`      | `MAX_ITER`, `API_TOKEN`    | Used for global constants. Not intended to be changed. |

## Notes

- **Repository names** often use `kebab-case` for readability in URLs, but this does **not** translate to importable module names.
- **Modules** must use `snake_case` instead as because Python does not allow hyphens (`-`) in identifiers.
