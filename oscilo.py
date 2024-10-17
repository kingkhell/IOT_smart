sudo raspi-config ,interface,I2c,Enbale
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essentail python3-dev python3-smbus git
git clone https://github.com/adafruit/Adafruit_Python_ADS1x15.git

ls
cd Adafruit_Python_ADS1x15
sudo python setup.py install
sudo apt-get install python-matplotlib
#VDD Pin 17 
#GND Pin 9
#SCL Pin 5
#SDA Pin 3

