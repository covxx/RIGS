#MSS 2021 | Alpha V0.2 - Status: Working
# Copyright Christian Jensen @covxx
# Contact cmjensenx@gmail.com
import subprocess
import threading
import sys
import select
import os
import os.path
from pathlib import Path
from configparser import ConfigParser
config_object = ConfigParser()
from sense_hat import SenseHat
sense = SenseHat()
sense.clear()
sense.clear(255, 0, 0)
pbar = sense.get_pressure()
tmp = sense.get_temperature()
humD = sense.get_humidity()
setf = Path("config.ini") #Path For Config File
arun = 'F' #var for first time check, gets over written by ftrun()
def clear_S(): #Call back for screen clearing
    os.system('cls' if os.name == 'nt' else 'clear') #Cross Platofrm scren clear
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
    clear_S()
    f= open('config.ini',"w+") #Creates config file
    global arun #Set arun to global status, this is done twice to make sure the var gets updated
    arun = "True"
    print(arun)
    main_Menu()
def main_Menu():
    clear_S()
    sense.clear()
    sense.clear(0, 255, 0)
    #print(arun) #Debug for first time check
    print ("Welcome to Robin Farming Intrustment")
    print ("----------------------------------------------")
    print("1. Start Data Logging") #Run data logging session
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
        #settings() #| | Not implemented
    elif mmi == 4: #May need to create a end prog function to close any open data filesd
        clear_S()
        print ("Shuting down application")
        exit() #Closes program
    else:
        main_Menu()
def sm(): #Menu Option Two
    clear_S()
    sense.clear(0, 255, 0)
    print ("Manual Data Logging Menu") #Prints infomation without saving data to file\server
    print ("1. Temperature") #Prints Temp
    print ("2. Humidity") #Print Humidity
    print ("3. Pressure") #Prints Pressure
    print ("4. Main Menu") #Back to main menu
    print ("----------------------------------------------")
    smi = int(input("Enter number selection to proceed:  "))
    if smi == 1:
        print ("Loading...")
        g_tp() #In progress
    elif smi == 2:
        print ("Loading...")
        hum()
    elif smi == 3:
        print ("Loading...")
        pbar()
    elif smi == 4:
        print("Loading main menu..")
    else: #Any other number re-runs menu
        sm()
        main_Menu()
def pbar():
    clear_S()
    sense.clear()
    mdls_pbar = round(sense.get_pressure()) #rounds pressure reading
    print("Current Zone pressure Level:", mdls_pbar,"milliebars") #Sensehat unit is milliebars, future will convert
    input("Press any key to return to menu") #place holder for testing
    main_Menu()
def hum():
    clear_S()
    sense.clear()
    mdls_hum = sense.get_humidity()
    print("Current Zone Humidity Level:", mdls_hum,"%")
    input("Press any key to return to menu") #place holder for testing
    main_Menu()
def g_tp():
    clear_S()
    sense.clear()
    sense.clear(0, 0, 255)
    mdls_temp = round(sense.get_temperature()*9/5+32)
    print("Current Zone temperature:", mdls_temp,"F") #This will need to be looped with polling of every 3seconds
    input("Press any key to return to menu")
    main_Menu() #loop back to mm for testing, will be changed after loop
def start_dls(): #Data Logging start, loads config file to start //In Progress
#Config file needs to have user set parm to log (temp,Humidity,pressure)
#Needs to print current data
    clear_S()
    sense.clear()
    dls_temp = round(sense.get_temperature()*9/5+32)
    print ("Starting data logging session...")
    #while true:
    print("Current Zone temperature:", dls_temp,"F") #This will need to be looped with polling of every 3seconds
ftrun() #Check for first time setup - start program workflow
