#!/bin/sh
set -e
python app/manage.py makemigrations
python app/manage.py migrate
python app/manage.py collectstatic --no-input
sh -c "cd /service/app/ && gunicorn --workers 5 --timeout 60 --bind 0.0.0.0:7000 conf.wsgi:application --daemon && nginx -g 'daemon off;'"
exec "$@"