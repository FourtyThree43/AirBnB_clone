#!/usr/bin/env bash

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(git -C "$SCRIPT_DIR" rev-parse --show-toplevel)"

set -x

# see also ".mailmap" for how email addresses and names are deduplicated
cat > "${ROOT_DIR}/AUTHORS" <<- EOF
	# File @generated by myScripts/generate-authors.sh. DO NOT EDIT.
	# This file lists all contributors to the repository.
	# See myScripts/generate-authors.sh to make modifications.
	$(git -C "$ROOT_DIR" log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf)
EOF
