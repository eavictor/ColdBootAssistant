#!/usr/bin/env bash

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

python3 -m pip install --upgrade pip
python3 -m pip install --upgrade setuptools
pip3 install -Ur requirements.txt

cp ./service/ColdBootAssistant.service /lib/systemd/system/ColdBootAssistant.service
sudo chmod 644 /lib/systemd/system/ColdBootAssistant.service
sudo chmod +x /home/pi/ColdBootAssistant/main.py
sudo systemctl daemon-reload
sudo systemctl enable schedule_camera.service
sudo systemctl start schedule_camera.service
exit 0