#!/bin/bash

set -e

cd "`dirname \"$0\"`"

if [ -n "$PYPI_USER" ] && [ -n "$PYPI_PASSWORD" ]; then
  echo "Variables PYPI_USER and PYPI_PASSWORD are present."
else
  echo "Variables PYPI_USER and PYPI_PASSWORD are expected but not found."
  exit 1
fi

echo "[distutils]
index-servers =
    pypi

[pypi]
username:$PYPI_USER
password:$PYPI_PASSWORD
" > ~/.pypirc
