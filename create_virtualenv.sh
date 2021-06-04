#!/bin/bash -e

CWD="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PYTHON_BIN=$(which python3)
VIRTUALENV_BIN=$(which virtualenv)

# Check dependencies
if [ ! -f ${PYTHON_BIN} ]; then
  echo "Please install system dependencies, exiting ..."
  exit 1
fi

if [ ! -f ${VIRTUALENV_BIN} ]; then
  pip install virtualenv
fi


# Remove virtual env if present
if [ -d .venv ]; then
  rm -rf .venv
fi


# Create virtual environment
virtualenv -p ${PYTHON_BIN} .venv
source ./.venv/bin/activate
pip install -r ${CWD}/requirements.txt

echo "To enable python env type: "
echo "source ${CWD}/.venv/bin/activate"
