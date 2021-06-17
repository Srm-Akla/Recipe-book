#!/usr/bin/python3
#
# TO-DO -> 
#----------------------------------------
#Imports
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import argparse
import gspread
from bs4 import BeautifulSoup 
import requests
#-----------------------------------
def art():
    print(" _________________") 
    print("|  _____________  |")
    print("| |             | |")
    print("| | Recipe Book | |")
    print("| |_____________| |")
    print("|_________________|")
    print("\n")


#function for arguments
def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--sheet', help='Select Sheets - Breakfast, Lunch, Dinner, Snacks, Desert', type=str)
    parser.add_argument('-new','--new_row', help='Input new recipe', default=False, action='store_true')
    parser.add_argument('-get','--get_values', help='Get all recipes ', default=False, action='store_true')
    parser.add_argument('-del','--del_rows', help='Delete recipe', default=False, action='store_true')
    parser.add_argument('-mod','--mod_values', help='Modify recipe values', default=False, action='store_true')
    return parser.parse_args()
#--------------------------------------
#Input data 
header = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0"}

def input_val():
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
def get_val():
    #Selects the data from A2 to the end
    values = worksheet.get_all_values()
    #worksheet.update("Bing!")
    #print(values)
    num = 1
    for row in values:
        print('\033[38;2;53;210;207m%d | \033[38;2;114;152;206m%s | \033[38;2;101;190;206m %s | \033[38;2;255;241;208m%s | \033[38;2;241;175;37m%s | \033[38;2;201;102;0m%s | \033[38;2;175;123;94m%s \033[00m' % (num, row[0], row[1], row[2], row[3], row[4], row[5]))
        num = num + 1
        #print(row)
#----------------------------
#Delete rows
def del_val():
    row_number=int(input("Enter Row number to delete: "))
    worksheet.delete_rows(row_number) 

#Modify recipes
def mod_val():
    row_number=int(input("Enter Row number to modify: "))
    col_number=int(input("Enter Column number to modify: "))
    val = input("Enter modification value for recipe: ")
    worksheet.update_cell(row_number, col_number, val)
#-----------------------------------------------
if __name__ == '__main__':
    #Api websites.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
    # The ID of spreadsheet - Recipe-book
    SPREADSHEET_ID = '1TkI-xOhjdIgIcq443KqUgFHcJJ-Asb4JJJg2O5gklxU'
    #Crendentials
    gc = gspread.service_account(filename='credentials.json')
    sh = gc.open_by_key(SPREADSHEET_ID)
    worksheet = sh.worksheet(args().sheet)
    
    art()
    
    if args().new_row:
        input_val()
    elif args().get_values:
        get_val()
    elif args().del_rows:
        del_val()    
    elif args().mod_values:
        mod_val()
    else:
        print("\033[1;33m No argument selected, please type - \033[1;31m 'python3 main.py -h' \033[00m")


