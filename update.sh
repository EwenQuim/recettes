#!/bin/zsh

bold=$(tput bold)
normal=$(tput sgr0)

# DEBUG
# set -euxo pipefail

cd /home/ubuntu/recettes

# Protecting bdd
cp db.sqlite3 ../backup_bdd

echo "\n${bold}→ GIT - Pulling source code${normal}"
git pull;

# Restoring bdd
rm -v db.sqlite3
mv -v ../backup_bdd/db.sqlite3 .


echo "\n${bold}→ PYTHON ENV - Activating virtualenv${normal}"
source ./env/bin/activate

echo "\n${bold}→ PYTHON ENV - Installing packages${normal}"
pip install -r requirements.txt

echo "\n${bold}→ DJANGO - Migrating Databases${normal}"
python manage.py makemigrations
python manage.py migrate

echo "\n${bold}→ DJANGO - Collecting static files${normal}"
python manage.py collectstatic --no-input

echo "\n${bold}→ SERVER - Copying server configuration${normal}"
sudo cp -v ops/gunicorn.conf /etc/systemd/system/gunicorn.service
sudo cp -v ops/nginx.conf /etc/nginx/sites-available/recettes
sudo ln -v -f -s /etc/nginx/sites-available/recettes /etc/nginx/sites-enabled/recettes

echo "\n${bold}→ SERVER - Reload Daemons${normal}"
sudo systemctl daemon-reload

echo "\n${bold}→ SERVER - Restarting gunicorn${normal}"
sudo systemctl restart gunicorn

echo "\n${bold}→ SERVER - Restarting nginx${normal}"
sudo systemctl restart nginx

echo "\n${bold}→ PYTHON ENV - Exiting virtualenv${normal}"
deactivate

echo "\n${bold}→ Updating successful!${normal}"
