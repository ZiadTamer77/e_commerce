#!/bin/bash

#wait for sql 
echo "Waiting for MySQL"
./wait-for-it.sh mysql:3306 --timeout=30 --strict -- echo "MY SQL is up"
# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# collecting statics
echo "Collecting Statics"
python manage.py collectstatic --noinput

echo "Creating superuser"
python manage.py create_superuser_if_none

# Start server
echo "Starting server"
exec gunicorn storefront.wsgi:application --bind 0.0.0.0:8000
