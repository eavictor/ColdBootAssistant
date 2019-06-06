=================
ColdBootAssistant
=================

--------
Behavior
--------

1. If Flask Service is installed, Start Flask Service.

2. Wait 60 seconds and start Cold Boot / Force Shutdown Assistant.

3. If Flask Service is installed, everyone can see current count.

-------------------
1. Install Raspbian
-------------------
1. Download Raspbian Lite from Here_.

.. _Here: https://www.raspberrypi.org/downloads/raspbian/

2. Unzip downloaded file.

3. Write image to Micro SD Card.

-----------------------------
2. Connect to WiFi (Optional)
-----------------------------
.. code-block:: bash

    sudo raspi-config

1. Choose 2 Network Options

2. Choose N2 Wi-fi

3. Select Country

4. Enter WiFi SSID

5. Enter WiFi Password

-------------------------------
3. Enable SSH Server (Optional)
-------------------------------

1. Enable SSH Server from raspi-config

2. Choose 5 Interfacing Options

3. Choose P2 SSH

4. Select <Yes>

5. Edit sshd_config

.. code-block:: bash

    sudo raspi-config

6. Uncomment these lines

.. code-block::

    #Port 22
    #AddressFamily any
    #ListenAddress 0.0.0.0
    #ListenAddress ::
    #LoginGraceTime 2m
    #PermitRootLogin prohibit-password
    #PasswordAuthentication yes
    #PermitEmptyPasswords no

7. Ctrl + O

8. Enter

9. Ctrl + X

10. Make sure SSH Service is enabled and reload SSH Service

.. code-block:: bash

    sudo service ssh enable
    sudo service ssh restart
    sudo service ssh status

-------------------
4. Install Services
-------------------

1. Install git

.. code-block:: bash

    sudo apt-get update
    sudo apt-get install -y git

2. Clone this repository

.. code-block:: bash

    git clone https://github.com/eavictor/ColdBootAssistant.git

3. Change Directory

.. code-block:: bash

    cd ColdBootAssistant

4. Change file owner (4 files)

.. code-block:: bash

    chown +x install1_python.sh
    chown +x install2_coldboot.sh
    chown +x install2_force_shutdown.sh
    chown +x install3_flask.sh

5. Install Python 3.7.3 (1st script)

.. code-block:: bash

    sudo bash install1_python.sh

6. Change user to root

.. code-block:: bash

    sudo -i

7. Install one of below service (2nd script)

.. code-block:: bash

    bash install2_coldboot.sh
    bash install2_force_shutdown.sh

8. Install Flask for showing cycle count (optional, 3rd script)

.. code-block:: bash

    bash install3_flask.sh

9. For Force Shutdown, install python 3.7.3 and dependencies and put pc_boot_complete.py to startup folder

--------------
Hardware parts
--------------
1. 1x Raspberry Pi 3 Model B
2. 1x Sharp PC817 (OPTO Isolator)
3. 1x Keyes Relay
4. 1x 1/4W 10kΩ Resistor
5. 1x 1/4W 1kΩ Resistor
6. 1x Breadboard
7. 3x Female-to-Female DuPont Wire (see below)
8. 8x Male-to-Female DuPont Wire (see below)
9. 1x MicroSD Card


.. important::
    Female-to-Female DuPont Wire

    1x red (RPi PIN 2 <--> Relay VCC PIN)

    1x black (RPi PIN 6 <--> Relay GND PIN)

    1x white (RPi PIN 12 <--> Relay IN1 PIN)

.. important::
    Male-to-Female DuPont Wire

    1x red (PC817 PIN 4 <--> RPi PIN 1)

    2x black (Breadboard - <--> RPi PIN 9)

    1x blue (PC817 PIN 3 <--> RPi PIN 3 <--> 1kΩ Resistor <--> Breadboard-)

    1x green (PC PowerLED+ <--> PC817 PIN 1)

    1x yellow (PC PowerLED- <--> PC817 PIN 2 10kΩ Resistor <--> Breadboard-)

    1x orange (Relay PIN 1 <--> PowerSW+)

    1x purple (Relay PIN 3 <--> PowerSW-)
