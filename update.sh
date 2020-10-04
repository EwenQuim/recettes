#!/bin/zsh

source ./env/bin/activate
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input
deactivate
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
