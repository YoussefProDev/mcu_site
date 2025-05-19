#!/bin/sh
python manage.py migrate
python manage.py collectstatic --noinput --clear
exec gunicorn mcu_site.wsgi:application --bind 0.0.0.0:8000
