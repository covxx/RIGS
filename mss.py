#MSS 2021 | Alpha V0.2.1 - Status: Working
# Copyright Christian Jensen CMXLABS
# Contact cmjensenx@gmail.com
import subprocess
import math
import threading
import sys
import select
import os
import os.path
from pathlib import Path
from configparser import ConfigParser
config_object = ConfigParser()
def ftrun(): #First time run check
    setf = Path("config.ini")
    if setf.is_file(): #checks if file exists
        global arun #Set arun to global status
        arun = "True"
        #print(arun) #Debug for first time check
        main_Menu() #Runs main menu
    else:
        ftsetup() #Runs first time setup
def ftsetup(): #First time setup config //In Progress
    f= open('config.ini',"w+") #Creates config file
    global arun #Set arun to global status, this is done twice to make sure the var gets updated
    arun = "True"
    print(arun)
    main_Menu()
def main_Menu():
    #print(arun) #Debug for first time check
    print ("Welcome to Robin Farming Intrustment")
    print ("----------------------------------------------")
    print ("1. Start Data Logging") #Run data logging session
    print ("2. Sensor Data") #Sub menu with sensor specific test
    print ("3. Settings") #Program settings
    print ("4. Shut Down") #Close Program
    print ("----------------------------------------------")
    mmi = int(input("Enter number selection to proceed:  "))
    if mmi == 1:
        print ("Loading...")
        start_dls() #| In Progress...
    elif mmi == 2:
        print ("Loading...")
        sm()
    elif mmi == 3:
        print ("Loading...")
        setng()
    elif mmi == 4: #May need to create a end prog function to close any open data filesd
        print ("Shuting down application")
        exit() #Closes program
    else:
        main_Menu()
def sm(): #Menu Option Two
    print ("Manual Data Logging Menu") #Prints infomation without saving data to file\server
    print ("1. Temperature") #Prints Temp
    print ("2. Humidity") #Print Humidity
    print ("3. Pressure") #Prints Pressure
    print ("4. Main Menu") #Back to main menu
    print ("----------------------------------------------")
    smi = int(input("Enter number selection to proceed:  "))
    if smi == 1:
        print ("Loading...")
       #In progress
    elif smi == 2:
        print ("Loading...")
    elif smi == 3:
        print ("Loading...")
    elif smi == 4:
        print("Loading main menu..")
        main_Menu()
    else: #Any other number re-runs menu
        sm()
        main_Menu()
def setng():
        print ("Settings Menu")
        print ("1. Device Config") #Config options
        print ("2. Data Logging Timer") #Change Data logging end timer
        print ("3. Testing") #Testing menu
        print ("4. Main Menu") #Back to main menu
        print ("----------------------------------------------")
        seti = int(input("Enter number selection to proceed:  "))
        if seti == 1:
            print ("Loading...")
            #dcon() #Not implemented //Device config
        elif seti == 2:
            print ("Loading...")
            #dlet() #Not implemented //Data Logging end timer
        elif seti == 3:
            print ("Loading...")
            #pbar() #Not implemented //Testing menu
        elif seti == 4:
            print("Loading main menu..")
            main_Menu()
        else: #Any other number re-runs menu
            setng()
ftrun() #Check for first time setup - start program workflow
