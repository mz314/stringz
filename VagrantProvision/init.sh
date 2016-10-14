apt-get -y install python3-pip postgresql libpq-dev postgresql-contrib
pip3 install virtualenv
sudo su - postgres -c 'psql -U postgres -c "CREATE DATABASE stringz"'
sudo su - root -c 'chmod a+rwx /etc/postgresql/9.3/main/pg_hba.conf'
echo "local all all trust" > /etc/postgresql/9.3/main/pg_hba.conf
echo "host all all   127.0.0.1/32  trust" >> /etc/postgresql/9.3/main/pg_hba.conf
service postgresql restart
su vagrant

virtualenv --python=python3 /home/vagrant/venv
source /home/vagrant/venv/bin/activate
cd /vagrant
pip install -r requirements.txt
pip install psycopg2
export DJANGO_SETTINGS_MODULE='stringz.settings_vagrant'
python3 ./manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'm@il.xx', 'test')" | python3 manage.py shell


