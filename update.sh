#!/bin/zsh

echo "GIT - Pulling source code"
git pull

echo "PYTHON ENV - Activating virtualenv"
source ./env/bin/activate

echo "PYTHON ENV - Installing packages"
pip install -r requirements.txt

echo "DJANGO - Migrating Databases"
python manage.py makemigrations
python manage.py migrate

echo "DJANGO - Collecting static files"
python manage.py collectstatic --no-input

echo "PYTHON ENV - Exiting virtualenv"
deactivate

echo "SERVER - Reload Daemons"
sudo systemctl daemon-reload

echo "SERVER - Restarting gunicorn"
sudo systemctl restart gunicorn

echo "Updating successful!"