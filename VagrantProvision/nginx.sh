sudo su
cp /home/vagrant/nginx.conf /etc/nginx/sites-available/django
rm /etc/nginx/sites-enabled/default 2> /dev/null
ln -sf /etc/nginx/sites-available/django /etc/nginx/sites-enabled/django
chmod a+rwx /home/vagrant/wsgi.py
sudo service nginx restart
uwsgi --ini /home/vagrant/uwsgi.ini 
