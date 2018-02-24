Application setup instructions:



Install python3.5

sudo apt-get install libssl-dev openssl

wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz

tar xzvf Python-3.5.2.tgz

cd Python-3.5.2

./configure

make

sudo make install


Create/Activate the virtual environment with python3.5

mkvirtualenv <your_new_virtual_env_name> -p /usr/bin/python3.5


If above step fails, then try

mkvirtualenv <your_new_virtual_env_name> -p /usr/local/bin/python3.5

### Database Setup


Install postgres 9.5 or above and create a new db named bb

##Create super User
python manage.py createsuperuser
