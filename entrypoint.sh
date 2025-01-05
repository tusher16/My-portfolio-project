#!/bin/sh

# Load environment variables from .env file
set -a
. /app/.env
set +a

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start Gunicorn
gunicorn portfolio.wsgi:application --bind 0.0.0.0:8000