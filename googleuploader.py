import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials

def get_worksheet(workSheetNumber, key):
    scope = [
    'https://spreadsheets.google.com/feeds/'
    ]
    credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/pi/Desktop/sukatan/credential.json', scope)
    gc = gspread.authorize(credentials)

    # Open a worksheet from spreadsheet with one shot
    wks = gc.open_by_key(key)
    # wks = gc.open_by_key("1tEI-UoGyEmq1YIeStnn3ngcbxhJT69v-R0zFTNVF79Q")
    wks = wks.get_worksheet(workSheetNumber)

    return wks

def upload_row_to_google_sheet(date, time, distance, key, worksheetIndex):
    wks = get_worksheet(int(worksheetIndex), key)

    # Finds where the Date and Distance cell
    distanceCell = wks.find('Distance')
    dateCell = wks.find('Date')
    timeCell = wks.find('Time')

    # Find the next row to be inserted
    try:
      nextRow = wks.col_values(1).index(date) + 1
    except:
      nextRow = wks.col_values(1).index('') + 1  

    # Insert the date
    wks.update_cell(nextRow, dateCell.col, date)

    # Insert the time
    wks.update_cell(nextRow, timeCell.col, time)
    
    # Insert the distance
    wks.update_cell(nextRow, distanceCell.col, distance)
    print "Sensor:" + str(worksheetIndex) + "| Uploaded cell | Date:" + date + " | Time: " + time + "| Distance:" + str(distance) + " | Row: " + str(nextRow)

def upload_realtime_reading_to_google_sheet(date, time, distance, key, lastWorksheetIndex, sensorIndex):
    # Get the last worksheet which is equivalent to the number of sensor since index starts at 0
    wks = get_worksheet(int(lastWorksheetIndex), key)

    dateCell = wks.find('Date')
    timeCell = wks.find('Time')
    distanceCell = wks.find('Distance')
    sensorCell = wks.find('Sensor')

    wks.update_cell(dateCell.row + 1 + int(sensorIndex), dateCell.col, date)
    wks.update_cell(timeCell.row + 1 + int(sensorIndex), timeCell.col, time)
    wks.update_cell(distanceCell.row + 1 + int(sensorIndex), distanceCell.col, distance)
    wks.update_cell(sensorCell.row + 1 + int(sensorIndex), sensorCell.col, sensorIndex)

    print "Sensor:" + str(sensorIndex) + " | Updated real time reading:" + " Date: " + date + "| Time: " + time + "| Distance: " + str(distance)

