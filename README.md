# console-logging

Better console logging for Python.

Find us on PyPi: https://pypi.python.org/pypi/console-logging


![Showcase](https://github.com/pshah123/console-logging/raw/master/images/example.png "Demo of console-logging")

## Getting Started

### Dependencies

* Python 2.6+ or Python 3.5+
* `termcolor`

### Installation

```
pip install console-logging
```

### Usage

```
from console_logging import console

console.log("Hello World!")
```


### Exhaustive Reference

```
console.log("This is a log.")
console.error("This is an error.")
console.info("This is some neutral info.")
console.success("This is a success message.")
```

### Example

For an exhaustive example, see `tests/example.py`.

### Credit

* `termcolor` module for colors