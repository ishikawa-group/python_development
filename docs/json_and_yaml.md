# Working with JSON, YAML, and TOML in Python

This guide explains common configuration formats and how to handle them in Python.

## Understanding JSON

JSON (JavaScript Object Notation) is a lightweight data format that uses:
- Objects: `{"key": "value"}`
- Arrays: `[1, 2, 3]`
- Basic data types:
  - Strings: `"Hello"`
  - Numbers: `42`, `3.14`
  - Booleans: `true`, `false`
  - Null: `null`

Example JSON structure:
```json
{
    "name": "John Doe",
    "age": 30,
    "isStudent": false,
    "hobbies": ["reading", "gaming"],
    "address": {
        "street": "123 Main St",
        "city": "Boston"
    }
}
```

## Understanding YAML

YAML (YAML Ain't Markup Language) is a human-readable data format that uses:
- Indentation for structure
- Key-value pairs: `key: value`
- Lists with dashes: `- item`
- Multiple document support with `---`
- Comments with `#`

Example YAML structure:
```yaml
# Personal information
name: John Doe
age: 30
isStudent: false
hobbies:
  - reading
  - gaming
address:
  street: 123 Main St
  city: Boston

# You can have multiple documents in one file
---
# Another document
settings:
  theme: dark
  notifications: true
```

## Understanding TOML

TOML (Tom's Obvious, Minimal Language) is designed to be easy to read and write with:
- Simple key-value pairs: `key = "value"`
- Tables (sections) in square brackets: `[section]`
- Array of tables: `[[section]]`
- Support for dates and times
- Comments with `#`

Example TOML structure:
```toml
# This is a TOML document

title = "TOML Example"

[owner]
name = "John Doe"
age = 30

[database]
server = "192.168.1.1"
ports = [ 8001, 8001, 8002 ]
enabled = true

[servers]

  # Indentation (tabs or spaces) is allowed but not required
  [servers.alpha]
  ip = "10.0.0.1"
  role = "frontend"

  [servers.beta]
  ip = "10.0.0.2"
  role = "backend"

[[fruits]]
name = "apple"
color = "red"

[[fruits]]
name = "banana"
color = "yellow"
```

## JSON in Python

Python's built-in `json` module makes it easy to work with JSON data.

### Reading JSON

```python
import json

# Reading from a JSON file
with open('config.json', 'r') as file:
    data = json.load(file)

# Parsing JSON string
json_string = '{"name": "John", "age": 30}'
data = json.loads(json_string)
```

### Writing JSON

```python
import json

data = {
    "name": "John",
    "age": 30,
    "cities": ["New York", "London"]
}

# Writing to a JSON file
with open('output.json', 'w') as file:
    json.dump(data, file, indent=4)

# Converting to JSON string
json_string = json.dumps(data, indent=4)
```

## YAML in Python

YAML handling requires the `PyYAML` package (`pip install PyYAML`).

### Reading YAML

```python
import yaml

# Reading from a YAML file
with open('config.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Parsing YAML string
yaml_string = """
name: John
age: 30
cities:
  - New York
  - London
"""
data = yaml.safe_load(yaml_string)
```

### Writing YAML

```python
import yaml

data = {
    "name": "John",
    "age": 30,
    "cities": ["New York", "London"]
}

# Writing to a YAML file
with open('output.yaml', 'w') as file:
    yaml.dump(data, file, default_flow_style=False)

# Converting to YAML string
yaml_string = yaml.dump(data, default_flow_style=False)
```

## TOML in Python

TOML handling requires the `tomli` package for reading (`pip install tomli`) and `tomli-w` for writing (`pip install tomli-w`).

### Reading TOML

```python
import tomli

# Reading from a TOML file
with open('config.toml', 'rb') as file:
    data = tomli.load(file)

# Parsing TOML string
toml_string = '''
title = "My Config"
[server]
host = "localhost"
port = 8080
'''
data = tomli.loads(toml_string)
```

### Writing TOML

```python
import tomli_w

data = {
    "title": "My Config",
    "server": {
        "host": "localhost",
        "port": 8080
    }
}

# Writing to a TOML file
with open('output.toml', 'wb') as file:
    tomli_w.dump(data, file)

# Converting to TOML string
toml_string = tomli_w.dumps(data)
```

## Key Differences

- JSON:
  - Most widely used for web APIs
  - Strict syntax, no comments
  - Limited data types
  - Language-independent

- YAML:
  - Human-readable with support for comments
  - Uses indentation for structure
  - Supports complex data types
  - Multiple documents in one file
  - Popular for configuration files

- TOML:
  - Explicit and easy to read
  - Excellent for configuration files
  - Built-in support for dates and times
  - Clear table (section) syntax
  - No indentation requirements
  - Growing popularity in Python projects (e.g., pyproject.toml)