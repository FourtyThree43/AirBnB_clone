#!/usr/bin/env bash

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(git -C "$SCRIPT_DIR" rev-parse --show-toplevel)"

set -x

# Find all test files and run them using unittest
# by use of discover
# python3 -m unittest discover tests

# or by specifing the directory.
python3 -m unittest discover -s "${ROOT_DIR}/tests" -p "test*.py"
