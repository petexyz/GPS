sudo apt-get -yq update
sudo apt-get -yq install gpsd gpsd-clients

sudo systemctl stop gpsd.socket
sudo systemctl disable gpsd.socket

sudo gpsd /dev/serial0 -F /var/run/gpsd.sock

