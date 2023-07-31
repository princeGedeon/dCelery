#!/bin/ash

echo "Check migrations"
python manage.py makemigrations

echo "Apply database migrations"
python manage.py migrate

exec "$@"
