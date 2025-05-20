#!/bin/sh
set -e  # Interrompe lo script se un comando fallisce

echo "🛠️ Eseguo le migrations..."
python manage.py migrate

echo "📦 Raccolgo i file statici..."
python manage.py collectstatic --noinput

echo Popola /app/media solo se è vuoto
if [ ! -d /app/media/images ] || [ -z "$(ls -A /app/media/images 2>/dev/null)" ]; then
  
  if [ -d /app/default_media ]; then
   echo "📁 La cartella /app/media/images non esiste o è vuota. Popolo il volume media..."
 
    cp -r /app/default_media/* /app/media/
  else
    echo "⚠️  Attenzione: /app/default_media NON esiste!"
  fi
else
  echo "📁 Il volume media è già popolato. Nessuna copia eseguita."
fi

# Avvia Gunicorn
echo "🚀 Avvio Gunicorn..."
exec gunicorn mcu_site.wsgi:application --bind 0.0.0.0:8000
