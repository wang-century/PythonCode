import os

os.system('yum -y groupinstall "Development tools" && yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel && yum install libffi-devel -y')
os.system('wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tar.xz && tar -xvJf Python-3.7.4.tar.xz')
os.system('mkdir /usr/local/python3 && cd Python-3.7.4 && ./configure --prefix=/usr/local/python3 && make && make install ')
os.system('ln -s /usr/local/python3/bin/python3 /usr/local/bin/python3')
os.system('ln -s /usr/local/python3/bin/pip3 /usr/local/bin/pip3')
