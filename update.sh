#!/bin/zsh

bold=$(tput bold)
normal=$(tput sgr0)

# DEBUG
set -euxo pipefail

echo "\n${bold}→ GIT - Pulling source code${normal}"
git pull;

echo "\n${bold}→ PYTHON ENV - Activating virtualenv${normal}"
source ./env/bin/activate

echo "\n${bold}→ PYTHON ENV - Installing packages${normal}"
pip install -r requirements.txt

echo "\n${bold}→ DJANGO - Migrating Databases${normal}"
python manage.py makemigrations
python manage.py migrate

echo "\n${bold}→ DJANGO - Collecting static files${normal}"
python manage.py collectstatic --no-input

echo "\n${bold}→ SERVER - Copying gunicorn configuration${normal}"
sudo cp -v gunicorn.conf /etc/systemd/system/gunicorn.service

echo "\n${bold}→ SERVER - Reload Daemons${normal}"
sudo systemctl daemon-reload

echo "\n${bold}→ SERVER - Restarting gunicorn${normal}"
sudo systemctl restart gunicorn

echo "\n${bold}→ PYTHON ENV - Exiting virtualenv${normal}"
deactivate

echo "\n${bold}→ Updating successful!${normal}"
