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
