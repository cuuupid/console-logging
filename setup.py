from setuptools import setup, find_packages
from codecs import open as copen
from os import path

here = path.abspath(path.dirname(__file__))

with copen(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

print(long_description)

long_description = """
console-logging
===============

|Codeship Status for pshah123/console-logging| |PyPI version| |Codacy
Badge|

Better console logging for Python.

Find us on PyPi: https://pypi.python.org/pypi/console-logging

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

*If building from source:* ``bash pipe`` from inside this repo.

Usage
~~~~~

New:
^^^^

::

    from console_logging.console import Console
    console = Console()

    console.log("Hello world!")

Old:
^^^^

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

Example
~~~~~~~

For an exhaustive example, see ``tests/example.py``.

Credit
~~~~~~

-  ``termcolor`` module for colors

.. |Codeship Status for pshah123/console-logging| image:: https://app.codeship.com/projects/aed26890-8fca-0135-1d5e-36d54fbb9242/status?branch=master
   :target: https://app.codeship.com/projects/250054
.. |PyPI version| image:: https://badge.fury.io/py/console-logging.svg
   :target: https://badge.fury.io/py/console-logging
.. |Codacy Badge| image:: https://api.codacy.com/project/badge/Grade/c6656875f3234dfb9ab6bd4aa509ff57
   :target: https://www.codacy.com/app/pshah123/console-logging?utm_source=github.com&utm_medium=referral&utm_content=pshah123/console-logging&utm_campaign=Badge_Grade
"""

setup(
    name='console-logging',
    version='0.0.5.0',
    description='Better, prettier commandline logging.',
    long_description=long_description,
    url='https://github.com/pshah123/console-logging',
    author='Priansh Shah',
    author_email='me@priansh.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='logging color colors commandline console error timestamp',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    # py_modules=["console"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['termcolor'],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={},

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=[],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
    },
)
