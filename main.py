import csv
import os
#import PyQt5
from twilio.rest import TwilioRestClient
import openpyxl

AUTH_SID = 'AC81044c6365ff9250ce1013f8e2aaa5df' # Twilio SID
TEST_SID = '1a2B3c4D' # 

AUTH_TOKEN = '51b4ea922fc9a7f8a28cda3cf51f8b4f' # Twilio Token
TEST_TOKEN = '1a2B3c4D' # 

test_mode = True

position = 'Position'#Position in the company. Probably won't use.
shift = 'dayshift'#Reference to a working shift. Will probably change as well.
poc = 'Point of Contact'#Person who is sending the message

if test_mode == False:
    token = AUTH_TOKEN
    sid = AUTH_SID
else:
    token = TEST_TOKEN
    sid = TEST_SID

client = TwilioRestClient(sid, token)

wb = openpyxl.load_workbook("CTS_Employee_Numbers.xlsx")
sheet = wb.get_sheet_by_name('Numbers')
col = sheet['C']

for cell in col:
    if test_mode == True:
        print(cell.value)
    elif test_mode == False:
        client.messages.create(
            to = cell.value,
            from_ = '6155551234', # put your own Twilio phone number here
            body = f'Need {position} to work {shift} today. If you can work, please call {poc}')


#Not sure where to put this
#def main():
    #pass

#if __name__ == "__main__":
    #execute program
    #main()
