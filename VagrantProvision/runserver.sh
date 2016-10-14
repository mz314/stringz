sudo su
source /home/vagrant/venv/bin/activate
cd /vagrant

export DJANGO_SETTINGS_MODULE='stringz.settings_vagrant'
python3 ./manage.py migrate
python3 ./manage.py runserver 0.0.0.0:80 &
