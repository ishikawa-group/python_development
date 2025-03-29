# Pathlib
* Pathlib provides an object-oriented interface to filesystem paths in Python.
* It is better than the traditional ways using `os.path` or `open`; see later for reasons.

## Import
* `pathlib` is the standard library so no need to install by `pip`.
```python
from pathlib import Path
```

## Creating Path Objects
```python
p = Path("file.txt")                    # Current directory
p = Path("/home/user/docs/file.txt")    # Absolute path
p = Path.home() / "docs" / "file.txt"   # Combine paths with /
from pathlib import Path

# finding the path where that Python file exists
p = Path(__file__).resolve()

# upper directory
p = Path(__file__).resolve().parent

# upper-upper directory
p = Path(__file__).resolve().parent.parent
```

## Common Operations
```python
p.exists()               # Check if path exists
p.is_file()              # Is it a file?
p.is_dir()               # Is it a directory?

# Directory operations
p.mkdir(parents=True)     # Create directory (and parents)
p.unlink()                # Delete file
p.rename("newname.txt")   # Rename/move file
```

## Path Information
```python
p.name                    # File name ("file.txt")
p.stem                    # File name without extension ("file")
p.suffix                  # File extension (".txt")
p.parent                  # Parent directory
```

## File Operations
```python
# Reading and writing
p.read_text()            # Read file as string
p.write_text("hello")    # Write string to file
```

## Examples
```python
from pathlib import Path
import glob

# Working with directories
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

# Processing multiple files
for file_path in Path("docs").glob("*.txt"):
    content = file_path.read_text()
    # Process content...
```

## Why Pathlib is Better Than Traditional File Handling
### Built-in Context Management
* Pathlib simplifies file operations by handling file opening and closing automatically.

```python
# Traditional way
with open('file.txt', 'r') as f:
    content = f.read()

# Pathlib way - cleaner
content = Path('file.txt').read_text()
```

### Intuitive Path Manipulation
* Working with file paths becomes more straightforward and readable.

```python
# Traditional way
import os
directory = os.path.dirname(os.path.abspath(file_path))
filename = os.path.basename(file_path)

# Pathlib way
from pathlib import Path
path = Path(file_path)
directory = path.parent
filename = path.name
```

### Object-Oriented File Operations
* File operations become more intuitive with method chaining and object-oriented syntax.
```python
# Pathlib way
file = Path('document.txt')
if file.exists():
    file.unlink()  # delete
    file.rename('new.txt')  # rename
    
# Traditional way
import os
if os.path.exists('document.txt'):
    os.remove('document.txt')
    os.rename('document.txt', 'new.txt')
```

### Simplified Pattern Matching
* File searching and pattern matching become more straightforward.
```python
# Traditional way
import glob
python_files = glob.glob('*.py')

# Pathlib way
python_files = list(Path().glob('*.py'))
```
