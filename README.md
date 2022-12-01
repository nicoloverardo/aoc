# Advent of Code

This repo contains my proposed solutions for the [Advent of Code](https://adventofcode.com/).

# Setup

## Linux

If on Linux, you can simply use the `Makefile` to setup everything you need. `cd` into the folder and then run:

```bash
make
```

It will take care of creating the virtual env, activating it, and installing the required packages.

## Windows

If on Windows, you will need to create manually the virtual env and then install the requirements. We currently use `virtualenv` and `pip`:

```bash
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip wheel setuptools
python -m pip install -r requirements.txt
```

# How to use

In order to run the script to display the solution, please:

1. Navigate into the _day_ folder:

```bash
cd 2022/Day\ 01/
```

2. Run the script:

```python
python solution.py
```

## Content

```
.
├── 2021
│   ├── Day 01
│   │   ├── day01.py
│   │   └── input.txt
│   ├── Day 02
│   │   ├── day02.py
│   │   └── input.txt
│   ├── Day 03
│   │   ├── day03.py
│   │   └── input.txt
│   ...
│
├── 2022
│   ├── Day 01
│   │   ├── day01.py
│   │   ├── input.txt
│   │   └── test_input.txt
│   ├── Day 02
│   │   ├── day02.py
│   │   ├── input.txt
│   │   └── test_input.txt
│   ├── Day 03
│   │   ├── day03.py
│   │   ├── input.txt
│   │   └── test_input.txt
│   ...
|
├── .gitignore
├── LICENSE
├── Makefile
├── pyproject.toml
├── README.md
└── requirements.txt
```
