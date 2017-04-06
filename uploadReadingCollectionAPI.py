from googleuploader import upload_row_to_google_sheet
import sys

def upload_collection_to_google_sheet(key):
    file = open('readingCollectionDB', 'r')
    lines = file.readlines()
    try:
        for line in lines:
            data = line.split(',')
            date = data[0].rstrip()
            time = data[1].rstrip()
            distance = data[2].rstrip()
            sensorIndex = data[3].rstrip()
            print "Upload row to google sheet from csv file"
            upload_row_to_google_sheet(date, time, distance, key, int(sensorIndex))
    finally:
        file.close()
        file = open('readingCollectionDB', 'w')
        file.write('')
        file.close()


