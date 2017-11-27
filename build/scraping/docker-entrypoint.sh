#!/bin/sh -l
set -eu

export PYTHONPATH=/var/lib/python3/app

if [ $# -ge 2 ] && [ "$1" = "--" ]; then
  shift
  set -x
  exec "$@"
else
  set -x
  exec python3 "$@"
fi
