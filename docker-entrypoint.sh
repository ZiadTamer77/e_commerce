#!/bin/bash

# wait for db
echo "Waiting for MySQL"
./wait-for-it.sh $DB_HOST:$DB_PORT --timeout=30 --strict -- echo "MySQL is up"

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# collecting statics
echo "Collecting Statics"
python manage.py collectstatic --noinput

# Start server
echo "Starting server"
exec gunicorn storefront.wsgi:application --bind 0.0.0.0:8000