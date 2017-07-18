how to run
/home/pi/Desktop/sukatan/sukatan XXXXXX-GOOGLE-DRIVE-KEY-XXXXXX 2

## Install the following dependency first
sudo pip install gspread

sudo pip install oauth2client

copy and paste credential.json

sudo apt-get install ssmtp (edit the conf file in /etc/ssmtp/ssmtp.conf)

make sure the client email in the credential.json is added as owner in the google sheet

## How to edit crontab
crontab -e

## How to view crontab job
crontab -l
 
## How to make an image 
sudo dd if=/dev/diskX of=/path/of/destination bs=1m (you can use diskutil list to view the name of SD card)

## How to install an image
sudo diskutil unmount /dev/diskX  (where diskX is the name of the SD card)
sudo dd if=/path/of/image of=/dev/diskX
