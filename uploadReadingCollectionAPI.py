from googleuploader import upload_row_to_google_sheet
import sys

def upload_collection_to_google_sheet(key):
    file = open('readingCollectionDB', 'r')
    lines = file.readlines()
    eraseDB = False
    try:
        for line in lines:
            data = line.split(',')
            date = data[0].rstrip()
            time = data[1].rstrip()
            distance = data[2].rstrip()
            sensorIndex = data[3].rstrip()
            result = upload_row_to_google_sheet(date, time, distance, key, int(sensorIndex))
            if result == True:
              eraseDB = True 
              print "Reading collection DB: uploading a row to google sheet."
            else:
              print "Something went wrong uploading DB to google sheet"
    finally:
        file.close()
        if eraseDB == True:
          file = open('readingCollectionDB', 'w')
          file.write('')
          file.close()


