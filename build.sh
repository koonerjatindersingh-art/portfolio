#!/usr/bin/env bash
pip install -r requirements.txt
python web/manage.py collectstatic --noinput
