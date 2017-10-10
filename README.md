# console-logging

[ ![Codeship Status for pshah123/console-logging](https://app.codeship.com/projects/aed26890-8fca-0135-1d5e-36d54fbb9242/status?branch=master)](https://app.codeship.com/projects/250054)

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

*If building from source:* `bash pipe` from inside this repo.

### Usage

#### New:

```
from console_logging.console import Console
console = Console()

console.log("Hello world!")
```

#### Old:

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

# If using the new usage:
console.setVerbosity(4) # verbosity from 1 - 5, in order:
'''
[1] Errors
[2] Successes
[3] Logs
[4] Info
[5] Secure
'''
console.mute() # shorthand for setVerbosity(0)

```

### Example

For an exhaustive example, see `tests/example.py`.

### Credit

* `termcolor` module for colors