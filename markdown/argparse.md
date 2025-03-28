# argparse
## Basic usage
* The `argparse` module is a convenient way to handle command-line arguments in Python. Here's a basic example:

```python
import argparse

parser = argparse.ArgumentParser(description="A simple CLI application")
args = parser.parse_args()
```

## Adding arguments
### Common argument parameters
* `default`: Set default value if argument is not provided
* `type`: Specify the type of argument (int, float, str, etc.)
* `help`: Help message for the argument
* `required`: Make the optional argument required
* `choices`: List of allowed values

### Examples
1. Basic optional argument with default value:
```python
parser.add_argument(
    "--name",
    default="world",
    help="Your name (default: world)"
)
```

2. Required argument with type conversion:
```python
parser.add_argument(
    "--age",
    type=int,
    required=True,
    help="Your age"
)
```

3. Argument with choices:
```python
parser.add_argument(
    "--color",
    choices=["red", "blue", "green"],
    default="blue",
    help="Choose a color"
)
```

4. Boolean flag:
```python
parser.add_argument(
    "--verbose",
    action="store_true",
    help="Enable verbose output"
)
```

## Simple complete example

```python
import argparse

parser = argparse.ArgumentParser(description="Process some data")

# Add arguments
parser.add_argument(
    "--input",
    default="input.txt",
    help="Input file path (default: input.txt)"
)

parser.add_argument(
    "--num-workers",
    type=int,
    default=4,
    help="Number of workers (default: 4)"
)

parser.add_argument(
    "--mode",
    choices=["fast", "normal", "careful"],
    default="normal",
    help="Processing mode (default: normal)"
)

parser.add_argument(
    "--debug",
    action="store_true",
    help="Enable debug mode"
)

# Parse arguments
args = parser.parse_args()

# Use the arguments
print(f"Input file: {args.input}")
print(f"Number of workers: {args.num_workers}")
print(f"Mode: {args.mode}")
print(f"Debug enabled: {args.debug}")
```

### Command-line usage

```bash
# Using defaults
python script.py

# Overriding defaults
python script.py --input data.txt --num-workers 8 --mode fast --debug
```
