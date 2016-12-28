import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials

def upload_to_google_sheet(date, distance, key):
    scope = [
    'https://spreadsheets.google.com/feeds/'
    ]
    credentials = ServiceAccountCredentials.from_json_keyfile_name('./credential.json', scope)
    gc = gspread.authorize(credentials)

    # Open a worksheet from spreadsheet with one shot
    wks = gc.open_by_key(key)
    # wks = gc.open_by_key("1tEI-UoGyEmq1YIeStnn3ngcbxhJT69v-R0zFTNVF79Q")
    # wks = gc.open_(title)
    wks = wks.get_worksheet(0)

    # Finds the next empty row 
    nextEmptyRow = wks.col_values(1).index('') + 1

    # Finds where the Date and Distance cell
    distanceCell = wks.find('Distance')
    dateCell = wks.find('Date')

    wks.update_cell(nextEmptyRow, dateCell.col, date)
    wks.update_cell(nextEmptyRow, distanceCell.col, distance)
    print "Uploaded cell | date:" + date + " | value:" + str(distance) + " | row: " + str(nextEmptyRow)
