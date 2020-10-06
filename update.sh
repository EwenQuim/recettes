#!/bin/zsh

bold=$(tput bold)
normal=$(tput sgr0)

echo "${bold}GIT - Pulling source code${normal}"
git pull

echo "${bold}PYTHON ENV - Activating virtualenv${normal}"
source ./env/bin/activate

echo "${bold}PYTHON ENV - Installing packages${normal}"
pip install -r requirements.txt

echo "${bold}DJANGO - Migrating Databases${normal}"
python manage.py makemigrations
python manage.py migrate

echo "${bold}DJANGO - Collecting static files${normal}"
python manage.py collectstatic --no-input

echo "${bold}PYTHON ENV - Exiting virtualenv${normal}"
deactivate

echo "${bold}SERVER - Reload Daemons${normal}"
sudo systemctl daemon-reload

echo "${bold}SERVER - Restarting gunicorn${normal}"
sudo systemctl restart gunicorn

echo "${bold}Updating successful!${normal}"