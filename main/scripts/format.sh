#!/bin/sh -e

#* If script triggers error, exit
# set -e

#* Show trace in terminal
set -x

cd ..

#* Sort imports one per line, so autoflake can remove unused imports
isort . 
autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place . --exclude=__init__.py,base.py

#* Lint with black and sirt with isort again
black .
isort --recursive --apply .


