#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python web/manage.py collectstatic --noinput
