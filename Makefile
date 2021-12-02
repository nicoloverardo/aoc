.PHONY: create activate install clean

VENV_NAME?=venv
PYTHON_PATH?=${VENV_NAME}/bin/python

create:
	python -m pip install virtualenv
	python -m venv venv
	make activate

activate: $(VENV_NAME)/bin/activate

install: activate
	${PYTHON_PATH} -m pip install --upgrade pip setuptools wheel
	${PYTHON_PATH} -m pip install -r requirements.txt

clean:
	rm -rf __pycache__
	rm -rf venv