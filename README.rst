ColdBootAssistant
=================

------------
Installation
------------
1. (optional) Enable SSH Server on Raspberry Pi

.. code-block:: bash

    sudo nano /etc/ssh/sshd_config
    sudo service ssh start

2. Install git

.. code-block:: bash

    sudo apt-get update
    sudo apt-get install -y git

3. Clone this repository

.. code-block:: bash

    git clone https://github.com/eavictor/ColdBootAssistant.git

4. Change Directory

.. code-block:: bash

    cd ColdBootAssistant

5. Change file owner (3 files)

.. code-block:: bash

    chown +x main.py
    chown +x install_1_python.sh
    chown +x install_2_service.sh

6. Install Python 3.7.3 (1st script)

.. code-block:: bash

    sudo bash install_1_python.sh

7. Change user to root

.. code-block:: bash

    sudo -i

8. Install service (2nd script)

.. code-block:: bash

    bash install_2_daemon.sh

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
