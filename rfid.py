'''SDA connects to Pin 24.

SCK connects to Pin 23.

MOSI connects to Pin 19.

MISO connects to Pin 21.

IRQ: Not required

GND connects to Pin 6.

RST connects to Pin 22.

3.3v connects to Pin 1.'''

 sudo raspi-config
 sudo apt-get update
 lsmod | grep spi
 sudo apt-get upgrade
sudo apt-get install python3-dev python 3-pip
 sudo pip3 install spidev
 sudo pip3 install mfrc522
