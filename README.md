# Prime Numbers

## Preamble

The project is a small project introducing an opinionated python project layout.

## Objective

The project's objective is to provide a small library for testing a given integer, if it is a prime number.
The library code is called from cli apps as well es jupyter notebooks. The integration is straight forward by
modifying the `PYTHONPATH` environment variable.

## Setup

Calling

```shell
pre-commit install
pip install -r requirements.txt
```

in a terminal should make for a soft start.


## Tools

Please have a look at the tools utilized by the project:

- [poetry]((https://python-poetry.org))
- [pre-commit](https://pre-commit.com)
- [black](https://black.readthedocs.io/en/stable/)
- [flake8](https://flake8.pycqa.org/en/latest/)

## JetBrain's IDEs

Please mark the folders

- `src/cli_apps`
- `src/lib`
- `src/notebooks`

as _Source Root_. This makes the library code accessible to all consumers. The companion shell scripts provide a small 
terminal integration. 

## Further Readings:

 - [Wikipedia: Primality_test](https://en.wikipedia.org/wiki/Primality_test)
