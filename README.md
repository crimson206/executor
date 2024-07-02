# exec_with_namespace

`exec_with_namespace` is a Python module that provides a convenient wrapper around the built-in `exec()` function, offering additional features and type safety.

## Features

- Execute single or multiple Python code strings
- Automatic indentation correction
- Type-hinted for better IDE support and code safety
- Simplified namespace management

## Installation

You can install this module using pip:

```
pip install exec-with-namespace
```

## Usage

Here's a basic example of how to use `exec_with_namespace`:

```python
from exec_with_namespace import exec_with_namespace

# Execute a single code string
namespace = {}
exec_with_namespace("""
def greet(name):
    return f"Hello, {name}!"

result = greet("World")
""", namespace)

print(namespace['result'])  # Output: Hello, World!

# Execute multiple code strings
namespace = {}
codes = [
    """
    x = 10
    y = 20
    """,
    """
    sum = x + y
    """
]
exec_with_namespace(codes, namespace)

print(namespace['sum'])  # Output: 30
```

## API

```python
def exec_with_namespace(
    code: Union[str, List[str]],
    namespace: Dict[str, Any],
    globals: Optional[Dict[str, Any]] = None,
    indent_patch: bool = True
) -> None:
```

- `code`: A string or list of strings containing Python code to execute.
- `namespace`: A dictionary that will be used as the local namespace for execution.
- `globals`: An optional dictionary to use as the global namespace. If not provided, an empty dictionary will be used.
- `indent_patch`: If True (default), automatically corrects indentation issues in the provided code.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.