#!/usr/bin/env bash

PYTHON_VERSION = 3.7.3

apt-get update
apt-get upgrade -y
apt-get dist-upgrade -y
apt-get install -y build-essential checkinstall libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev
apt-get install -y wget

wget https://www.python.org/ftp/python/$(PYTHON_VERSION)/Python-$(PYTHON_VERSION).tgz
tar xzf Python-$(PYTHON_VERSION).tgz
cd Python-$(PYTHON_VERSION)
./configure --enable-optimizations
make -j8 build_all
make -j8 install
cd ..

rm -r Python-$(PYTHON_VERSION)
rm Python-$(PYTHON_VERSION).tgz

rm /usr/local/bin/python3
ln -s /usr/local/bin/python3.7 /usr/local/bin/python3

rm /usr/local/bin/pydoc3
ln -s /usr/local/bin/pydoc3.7 /usr/local/bin/pydoc3

rm /usr/local/bin/pip3
ln -s /usr/local/bin/pip3.7 /usr/local/bin/pip3

rm /usr/local/bin/2to3
ln -s /usr/local/bin/2to3-3.7 /usr/local/bin/2to3

rm /usr/local/bin/pyvenv
ln -s /usr/local/bin/pyvenv-3.7 /usr/local/bin/pyvenv

rm /usr/bin/python3m
ln -s /usr/local/bin/python3.7m /usr/bin/python3m

rm /usr/local/bin/python3-config
ln -s /usr/local/bin/python3.7-config /usr/local/bin/python3-config

apt-get autoremove --purge