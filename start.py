#Robin 0.3 Update 
# Copyright Christian Jensen @covxx
# Contact cmjensenx@gmail.com
import sys
from sense_hat import SenseHat
import datetime
import glob
import requests
import os.path
from os import path
#Configuring sensehat
sense = SenseHat()
sense.clear() #clears data from sensehat
temp = round(sense.get_temperature()*9/5+32)
humi = round(sense.get_humidity())
mbar = round(sense.get_pressure())
#Main section starts now
def frun(): #Checks if data file has already been created  and configures if it does not
    if os.path.isfile('data.txt'):  #File
        print("Loading Program...")
        main_Menu() #Calls menu
    else:
        print("Configuring Robin software, please wait...") #Configures settings
        tf = open('data.txt', 'w+') #Creates data file
        main_Menu()

def get_temp(): #Prints temp and is EOP
    print ("The temperature is currently:" ,temp, "F")
def hum(): #Humidity
    print ("The humidity is currently:",humi, "%")

def pbar(): #Pressure
    print ("The pressure is currently:",mbar,"mbar")

def main_Menu():
    print ("Welcome to Robin Farming Intrustment")
    print ("Ver. 0.3 - 1/20")
   # print ("The time currently is:"), ctime.strftime("%Y-%M-%D %H:%m:s") #Says current time; WIP/ May remove
    print ("----------------------------------------------")
    print("1. Start Data Logging") #Run data logging session
    print ("2. Sensor Data") #Sub menu with sensor specific test
    print ("3. Settings") #Program settings
    print ("4. Shut Down") #Close Program
    print ("----------------------------------------------")
    # MMI = Main Menu Input // Get temp or quit
    mmi = int(input("Enter number selection to proceed:  "))
    #print(mmi) # Test EOF
    if mmi == 1:
        print ("Loading...")
        start_mss()
    elif mmi == 2:
        print ("Loading...")
        sub_m()
    elif mmi == 3:
        print ("Loading...")
        settings()
    elif mmi == 4:
        print ("Logging out...")
        #shtdwn() | Shutdown class is currently not implmented
        sys.exit()

def sub_m()#Sub menu
    print ("Manual Data Logging Menu,")
    print ("1. Temperature") #Prints Temp
    print ("2. Humidity") #Print Humidity
    print ("3. Pressure") #Prints Pressure
    print ("----------------------------------------------")
        smi = int(input("Enter number selection to proceed:  "))
        if smi == 1:
            print ("Loading...")
            get_temp()
        elif smi == 2:
            print ("Loading...")
            hum()
        elif smi == 3:
         print ("Loading...")
            pbar()

def settings(): #Settings menu, but no settings
    print("Nothings here")
    main_menu() #Goes back to main menu until theres funticans

def shtdwn(): #Log out process to close data logging and save to local FS and network
    exit()

frun() #Program starts 
