# MSS Debug 2021 | Alpha V0.2.2 |
#Copyright Christian Jensen // CMX Labs cxlabs@gmail.com
#2021_06_11_21
#---Start Head----
import subprocess
import math
import threading
import sys
import select
#------End-Head---
def main_Menu():
    #print(arun) #Debug for first time check
    print ("MSS Debug Menu")
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
        g_tp() #In progress
    elif smi == 2:
        print ("Loading...")
        g_hum()
    elif smi == 3:
        print ("Loading...")
        g_pbar()
    elif smi == 4:
        print("Loading main menu..")
        main_Menu()
    else: #Any other number re-runs menu
        sm()
        main_Menu()
def g_pbar():
    #mdls_pbar = round(sense.get_pressure()) #rounds pressure reading
    print("Current Zone pressure Level:", mdls_pbar,"milliebars") #Sensehat unit is milliebars, future will convert
    input("Press any key to return to menu") #place holder for testing
    main_Menu()
def g_hum():
    #mdls_hum = sense.get_humidity()
    print("Current Zone Humidity Level:", mdls_hum,"%")
    input("Press any key to return to menu") #place holder for testing
    main_Menu()
def g_tp():
#    mdls_temp = round(sense.get_temperature()*9/5+32)
#    print("Current Zone temperature:", mdls_temp,"F") #This will need to be looped with polling of every 3seconds
    input("Press any key to return to menu")
    main_Menu() #loop back to mm for testing, will be changed after loop
def start_dls(): #Data Logging start, loads config file to start //In Progress
#Config file needs to have user set parm to log (temp,Humidity,pressure)
#Needs to print current data
    logtim = 10 #Variable for log interval, will be set by settings menu and be a global var
#    dls_temp = round(sense.get_temperature()*9/5+32)
    print ("Starting data logging session...")
    log_end = time.time() + logtim 
#    while time.time() < t_end:
#        print("Current Zone temperature:", dls_temp,"F")
main_Menu() #Check for first time setup - start program workflow