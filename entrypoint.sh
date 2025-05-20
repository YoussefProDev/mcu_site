#!/bin/sh
set -e  # Interrompe lo script se un comando fallisce

echo "🛠️ Eseguo le migrations..."
python manage.py migrate

echo "📦 Raccolgo i file statici..."
python manage.py collectstatic --noinput

echo Popola /app/media solo se è vuoto
if [ -z "$(ls -A /app/media 2>/dev/null)" ]; then
  echo "📁 Popolo il volume media..."
  cp -r /app/default_media/ /app/media/
else
  echo "📁 Il volume media NON è vuoto, salto la copia iniziale."
fi

# Avvia Gunicorn
echo "🚀 Avvio Gunicorn..."
exec gunicorn mcu_site.wsgi:application --bind 0.0.0.0:8000
