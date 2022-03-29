# IoT for industry-opencv
Opencv object detection with opencv and raspberry pi

Used:
  - Raspberry PI 4 4GB
  - Raspberry PI camera
  - LED 
  - Resistor


Installation of Open CV:

Enablea camera:

pi@raspberrypi:~ $ sudo raspi-config
  
![Screenshot 2022-03-29 at 15 30 41](https://user-images.githubusercontent.com/59376179/160622689-b0b91a0e-3ca3-4ef9-a936-ad49a798dda3.png)

Then expand the filesystem also in the raspi-config menu via 'Advanced Options'

![Screenshot 2022-03-29 at 15 32 06](https://user-images.githubusercontent.com/59376179/160623107-a4b4b54a-1fcb-47d4-b61b-616c76546969.png)

### First, update and upgrade any existing packages with:

  - pi@raspberrypi:~ $ sudo apt-get update
  - pi@raspberrypi:~ $ sudo apt-get upgrade


### Install image I/O packages:

  - pi@raspberrypi:~ $ sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
  - pi@raspberrypi:~ $ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev 
  - pi@raspberrypi:~ $ sudo apt-get install libxvidcore-dev libx264-dev
  - pi@raspberrypi:~ $ sudo apt-get install libgtk2.0-dev
  - pi@raspberrypi:~ $ sudo apt-get install libatlas-base-dev gfortran


### Install package manegement tool pip

  - pi@raspberrypi:~ $ sudo apt-get install python3-pip

### Install Numpy

  - pi@raspberrypi:~ $ pip install numpy

### OpenCV from default Raspbian repository

  - pi@raspberrypi:~ $ apt list python*opencv*
  - pi@raspberrypi:~ $ sudo apt install python3-opencv 
  - pi@raspberrypi:~ $ apt show python3-opencv

  
