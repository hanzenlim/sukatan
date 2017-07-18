import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials

# Global variable
wks = ''

def get_gspread(key):
  global wks

  scope = [
   'https://spreadsheets.google.com/feeds/'
  ]

  if wks == '':
    credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/pi/Desktop/sukatan/sukatan.credential.json', scope)
    gc = gspread.authorize(credentials)
    wks = gc.open_by_key(key)
    return wks
  else:
    return wks
    
def get_config_from_worksheet(key):
  print "Reading config from google sheet"
  worksheet = get_gspread(key)
  configSheet= worksheet.worksheet('config')
  configData = {}
  
  # Get sensor count.
  sensorCountCell = configSheet.find('sensorCount')
  row = sensorCountCell.row
  column = sensorCountCell.col + 1
  sensorCountCellValue = configSheet.cell(row, column)
  configData["sensorCount"] = sensorCountCellValue.value

  # Get dailyLogHour
  dailyLogHourCell = configSheet.find('dailyLogHour')
  row = dailyLogHourCell.row
  column = dailyLogHourCell.col + 1
  dailyLogHourCellValue = configSheet.cell(row, column)
  configData["dailyLogHour"] = dailyLogHourCellValue.value

  return configData


def get_worksheet_by_index(workSheetNumber, key):
  worksheet = get_gspread(key)

  return worksheet.get_worksheet(workSheetNumber)


def get_worksheet_by_name(name, key):
  worksheet = get_gspread(key)
  
  return worksheet.worksheet(name)


def upload_row_to_google_sheet(date, time, distance, key, sensorIndex):
    wks = get_worksheet_by_name("Sensor " + str(sensorIndex + 1), key)

    # Finds where the Date and Distance cell
    distanceCell = wks.find('Distance')
    dateCell = wks.find('Date')
    timeCell = wks.find('Time')

    # Find the next row to be inserted.
    # Gets all the values in the Date column and finds the next empty row.
    try:
      nextRow = wks.col_values(1).index(date) + 1
    except:
      nextRow = wks.col_values(1).index('') + 1  

    # Insert the date
    wks.update_cell(nextRow, dateCell.col, date)

    # Insert the time
    wks.update_cell(nextRow, timeCell.col, time)
    
    # Insert the distance
    try:
      distanceCellCol = wks.row_values(nextRow).index('') + 1
      wks.update_cell(nextRow, distanceCellCol, distance)
      print "Sensor:" + str(sensorIndex + 1) + "| Uploaded daily log | Date:" + date + " | Time: " + time + "| Distance:" + str(distance) + " | Row: " + str(nextRow)
      return True
    except:
      return False

def upload_realtime_reading_to_google_sheet(date, time, distance, key, sensorIndex):
    # Get the last worksheet which is equivalent to the number of sensor since index starts at 0
    wks = get_worksheet_by_name('Real time reading', key)

    dateCell = wks.find('Date')
    timeCell = wks.find('Time')
    distanceCell = wks.find('Distance')
    sensorCell = wks.find('Sensor')

    wks.update_cell(dateCell.row + 1 + int(sensorIndex), dateCell.col, date)
    wks.update_cell(timeCell.row + 1 + int(sensorIndex), timeCell.col, time)
    wks.update_cell(distanceCell.row + 1 + int(sensorIndex), distanceCell.col, distance)
    wks.update_cell(sensorCell.row + 1 + int(sensorIndex), sensorCell.col, sensorIndex + 1)

    print "Sensor:" + str(sensorIndex + 1) + " | Updated real time reading:" + " Date: " + date + "| Time: " + time + "| Distance: " + str(distance)

