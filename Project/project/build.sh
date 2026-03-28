#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input --settings=project.settings
python manage.py migrate --settings=project.settings