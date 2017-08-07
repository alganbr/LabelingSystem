#!/usr/bin/env bash

apt-get update
apt-get install -y apache2 python-pip python-dev libpq-dev postgresql postgresql-contrib libjpeg-dev

rm -rf /var/www
ln -fs /vagrant /var/www

# Install python requirements
pip install -r /home/vagrant/labelingsystem/requirements.txt

# Create database and syncdb
echo "ALTER USER postgres PASSWORD 'postgres'" | sudo -u postgres psql
pushd /home/vagrant/labelingsystem
./makemigrations.sh
/usr/bin/python manage.py migrate
/usr/bin/python manage.py generate_admin_group
popd

# Give everything in home folder back to vagrant user
chown -R vagrant:vagrant /home/vagrant
