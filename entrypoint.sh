#!/bin/sh
python manage.py migrate
python manage.py collectstatic --noinput
exec gunicorn mcu_site.wsgi:application --bind 0.0.0.0:8000
