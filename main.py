#!/usr/bin/python3
#
# TO-DO -> Add to database, get recipe based on headings, 
#----------------------------------------
#Imports
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import argparse
import gspread

#------------------------------------------
#Api websites.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive' ]
# The ID of spreadsheet - Recipe-book
SPREADSHEET_ID = '1TkI-xOhjdIgIcq443KqUgFHcJJ-Asb4JJJg2O5gklxU'

#-----------------------------------
#function for arguments
def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-be','--breakfast', help='Select Breakfast sheet', default=False, action='store_true')
    parser.add_argument('-lu','--lunch', help='Select Lunch sheet', default=False, action='store_true')
    parser.add_argument('-di','--dinner', help='Select Dinner sheet', default=False, action='store_true')
    parser.add_argument('-de','--desert', help='Select Desert sheet', default=False, action='store_true')
    return parser.parse_args()
#--------------------------------------
#Access google sheets
def api():
    gc = gspread.service_account(filename='credentials.json')
    sh = gc.open_by_key(SPREADSHEET_ID)
    #Selects worksheet based on arguments.
    if args().breakfast:
        worksheet = sh.worksheet("Breakfast")
    elif args().lunch:
        worksheet = sh.worksheet("Lunch")
    elif args().dinner:
        worksheet = sh.worksheet("Dinner")
    elif args().desert:
        worksheet = sh.worksheet("Desert")
    else:
        worksheet = sh.worksheet("Breakfast")

    #Selects the data from A2 to the end
    values = worksheet.get_all_values()
    #worksheet.update("Bing!")
    print(sh.worksheets()[1])

    for row in values:
        print('%s, %s' % (row[0], row[1]))


if __name__ == '__main__':
    api()
