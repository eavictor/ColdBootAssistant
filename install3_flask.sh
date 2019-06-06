#!/usr/bin/env bash

SERVICE_NAME="FlaskWebServer.service"
PY_FILE="web/webapp.py"

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

cp ./service/$(SERVICE_NAME) /lib/systemd/system/$(SERVICE_NAME)
sudo chmod 644 /lib/systemd/system/$(SERVICE_NAME)
sudo chmod +x /home/pi/ColdBootAssistant/$(PY_FILE)
sudo systemctl daemon-reload
sudo systemctl enable $(SERVICE_NAME)
sudo systemctl start $(SERVICE_NAME)
exit 0