import csv
import os
from twilio.rest import Client #TwilioRestClient
import openpyxl

AUTH_SID = '##########' # Twilio SID
TEST_SID = '#########' # 

AUTH_TOKEN = '###########' # Twilio Token, --take out of public repo--
TEST_TOKEN = '###########' # 

test_mode = True

if test_mode == False:
    token = AUTH_TOKEN
    sid = AUTH_SID
    client = Client(sid, token)#TwilioRestClient(sid, token)
else:
    token = TEST_TOKEN
    sid = TEST_SID
    #client = Client(sid, token)#TwilioRestClient(sid, token)



wb = openpyxl.load_workbook("CTS_Employee_Numbers.xlsx")
shtNames = wb.sheetnames()
sheet = wb['Test']
col = sheet['C']
rowObj =tuple(sheet['A:C'])

#how to go row by row, so I can access names with appropriate numbers?

for cell in col:
    if test_mode == True:
        print(shtNames)
    elif test_mode == False:
        if cell.value:
            client.messages.create(
                to = cell.value,
                from_ = '+12057231125', # put your own Twilio phone number here
                body = 'This is a Crown Technical Systems emergency text test')


#Not sure where to put this
#import PyQt5
##def main():
    #pass

#if __name__ == "__main__":
    #execute program
    #main()
