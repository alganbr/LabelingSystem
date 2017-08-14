#!/usr/bin/env bash

apt-get update
apt-get install -y apache2 python3-pip python3-dev libpq-dev postgresql postgresql-contrib libjpeg-dev

rm -rf /var/www
ln -fs /vagrant /var/www

# Install python requirements
pip3 install -r /home/vagrant/labelingsystem/requirements.txt

# Create database and syncdb
echo "ALTER USER postgres PASSWORD 'postgres'" | sudo -u postgres psql
alias python=/usr/bin/python3
pushd /home/vagrant/labelingsystem
./deletemigrations.sh
./makemigrations.sh
/usr/bin/python3 manage.py migrate
popd

# Give everything in home folder back to vagrant user
chown -R vagrant:vagrant /home/vagrant