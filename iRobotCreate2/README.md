# Python Controller Code for the iRobot Create 2

Install this code onto a Raspberry Pi, which should be connected to the create via the USB-\>Serial cable.

## Install

    pip install pyserial
    pip install pycreate2

## Find your communication port

You'll need to know the port on which the Raspberry Pi sends communications via the serial cable. Plug in the USB cable, then:

    dmesg | grep ttyUSB

You should see something similar to 

    ... FTDI USB Serial Device converter now attached to ttyUSB0

In this case, `ttyUSB0` is our communication port. You'll need this value in control.py 

## Control the robot

    python control.py

## Other libraries you could try:

* [Create2Control](https://github.com/pomeroyb/Create2Control)
* [BreezyCreate2](https://github.com/simondlevy/BreezyCreate2)
* [PythonRobot](https://github.com/Tall67Paul/PythonRobot)

## Credit

Based off of 

* [https://github.com/MomsFriendlyRobotCompany/pycreate2](https://github.com/MomsFriendlyRobotCompany/pycreate2)