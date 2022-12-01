.PHONY: all create install clean

VENV_NAME := venv
PYTHON_PATH := ${VENV_NAME}/bin/python


$(VENV_NAME)/bin/activate:
	python -m pip install virtualenv
	python -m venv $(VENV_NAME)
	${PYTHON_PATH} -m pip install --upgrade pip wheel setuptools
	${PYTHON_PATH} -m pip install --upgrade pip setuptools wheel
	${PYTHON_PATH} -m pip install -r requirements.txt


create: $(VENV_NAME)/bin/activate
all: $(VENV_NAME)/bin/activate

clean:
	rm -rf __pycache__
	rm -rf venv
