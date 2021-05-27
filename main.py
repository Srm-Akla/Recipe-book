#!/usr/bin/python3
#
# TO-DO -> Add to database, get recipe based on headings, 
#----------------------------------------
#Imports
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import argparse
import gspread
from bs4 import BeautifulSoup 
import requests
import re
#-----------------------------------
#function for arguments
def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--sheet', help='Select Sheets - Breakfast, Lunch, Dinner, Snacks, Desert', type=str)
    parser.add_argument('-new','--new_values', help='Input new recipe', default=False, action='store_true')
    parser.add_argument('-get','--get_values', help='Get recipe', default=False, action='store_true')
    return parser.parse_args()
#--------------------------------------
#Input data 

header = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0"}

def input_values():
    tags=input("Enter Tags for recipe: ")
    url=input("Paste URL for recipe: ")
    time=input("Entre Time for recipe: ")
    main=input("Enter Main Ingredient for recipe: ")
    difficulty=input("Enter Difficulty Level for recipe: ")

    page = requests.get(url, headers=header).text
    soup = BeautifulSoup(page, "lxml")
    name = soup.title.text
    
    worksheet.append_row([tags, name, url, time, main, difficulty], value_input_option="USER_ENTERED", insert_data_option="INSERT_ROWS")
    
#--------------------------------------
#Access google sheets
def get_values():
    #Selects the data from A2 to the end
    values = worksheet.get_all_values()
    #worksheet.update("Bing!")
    #print(values)
    for row in values:
        print('\033[32m%s | \033[31m %s | \033[33m%s | \033[34m%s | \033[35m%s | \033[36m%s \033[00m' % (row[0], row[1], row[2], row[3], row[4], row[5]))
        #print(row)
#-----------------------------------------------
if __name__ == '__main__':
    #Api websites.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
    # The ID of spreadsheet - Recipe-book
    SPREADSHEET_ID = '1TkI-xOhjdIgIcq443KqUgFHcJJ-Asb4JJJg2O5gklxU'
    gc = gspread.service_account(filename='credentials.json')
    sh = gc.open_by_key(SPREADSHEET_ID)
    worksheet = sh.worksheet(args().sheet)

    if args().new_values:
        input_values()
    elif args().get_values:
        get_values()
