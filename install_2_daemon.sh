#!/usr/bin/env bash

python3 -m pip install --upgrade pip
python3 -m pip install --upgrade setuptools
pip3 install -Ur requirements.txt
cp ./supervisor_conf/supervisord.conf /etc/supervisord.conf
supervisord -c /etc/supervisord.conf