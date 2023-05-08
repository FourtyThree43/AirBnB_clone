#!/usr/bin/env bash

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(git -C "$SCRIPT_DIR" rev-parse --show-toplevel)"

set -x

# Find all Python files and filter out any directories
python_files=$(find . -type f -name "*.py")

# Check each Python file for module, class, and function documentation
# for file in $python_files; do
#   # Check for module documentation
#   module_doc=$(python3 -c "import $(basename ${file%.py}); print($(basename ${file%.py})" "__doc__)")
#   if [ -z "$module_doc" ]; then
#     echo "Missing module documentation in file: $file"
#   fi

  # Check for class documentation
  # classes=$(python3 -c "import $(basename ${file%.py)}; print([c.__name__ for c in $(basename ${file%.py)}.__dict__.values() if isinstance(c, type)])")
  # for class_name in $classes; do
  #   class_doc=$(python3 -c "import $(basename ${file%.py)}; print($(basename ${file%.py)}.$class_name" "__doc__)")
  #   if [ -z "$class_doc" ]; then
  #     echo "Missing class documentation in file: $file (class $class_name)"
  #   fi

    # Check for function documentation inside the class
  #   functions=$(python3 -c "import $(basename ${file%.py)}; print([f for f in $(basename ${file%.py)}.$class_name.__dict__.values() if callable(f)])")
  #   for function in $functions; do
  #     function_doc=$(python3 -c "import $(basename ${file%.py)}; print($(basename ${file%.py)}.$class_name.$function" "__doc__)")
  #     if [ -z "$function_doc" ]; then
  #       echo "Missing function documentation in file: $file (class $class_name, function $function)"
  #     fi
  #   done
  # done

  # Check for function documentation outside of a class
  # functions=$(python3 -c "import $(basename ${file%.py)}; print([f.__name__ for f in $(basename ${file%.py)}.__dict__.values() if callable(f)])")
  # for function_name in $functions; do
  #   function_doc=$(python3 -c "import $(basename ${file%.py)}; print($(basename ${file%.py)}.$function_name" "__doc__)")
  #   if [ -z "$function_doc" ]; then
  #     echo "Missing function documentation in file: $file (function $function_name)"
  #   fi
  # done
# done

