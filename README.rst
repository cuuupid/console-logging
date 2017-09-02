console-logging
===============

Better console logging for Python.

.. figure:: https://github.com/pshah123/console-logging/raw/master/images/example.png
   :alt: Demo of console-logging

   Showcase

Getting Started
---------------

Dependencies
~~~~~~~~~~~~

-  Python 2.6+ or Python 3.5+
-  ``termcolor``

Installation
~~~~~~~~~~~~

::

    pip install console-logging

Usage
~~~~~

::

    from console_logging import console

    console.log("Hello World!")

Exhaustive Reference
~~~~~~~~~~~~~~~~~~~~

::

    console.log("This is a log.")
    console.error("This is an error.")
    console.info("This is some neutral info.")
    console.success("This is a success message.")

Example
~~~~~~~

For an exhaustive example, see ``tests/example.py``.

Credit
~~~~~~

-  ``termcolor`` module for colors