#Main program for Robin
# Copy right Christian Jensen @covxx
# Contact cmjensenx@gmail.com
#
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
#Start of program
def main(): #Checks if data file has already been created  and configures if it does not
    if os.path.isfile('data.txt'):  #File
            print("Loading Program...")
            main_Menu() #Calls menu
    else:
        print("Configuring Robin software, please wait...") #Configures settings
        tf = open('data.txt', 'w+') #Creates data file

        main_Menu()

def get_temp(): #Prints temp and is EOP
    print ("The temperature is currently:" ,temp, "F")
 #   tf.write(sense.temp) | Starting work on data logging to local FS
  #  tf.write('\n')
   # tf.writeclose()
    #sleep(50)
def hum(): #Humidity
     print ("The humidity is currently:",humi, "%")

def pbar #Pressure
    print ("The pressure is currently:",mbar,"mbar")
    
def main_Menu():
    print ("Welcome to Robin Farming Intrustment")
    print ("Ver. 0.1.5 - 10/17/19")
   # print ("The time currently is:"), ctime.strftime("%Y-%M-%D %H:%m:s") #Says current time; WIP/ May remove
    print ("----------------------------------------------")
    print ("1. Temperature") #Prints Temp
    print ("2. Humidity") #Print Humidity
    print ("3. Pressure") #Prints Pressure
    print ("4. Quit") #Close Program
    print ("5. Settings") #Program settijgs
    print ("----------------------------------------------")
    # MMI = Main Menu Input // Get temp or quit
    mmi = int(input("Enter number selection to proceed:  "))
    #print(mmi) # Test EOF
    if mmi == 1:
        print ("Loading...")
        get_temp()
    elif mmi == 2:
        print ("Loading...")
        hum()
    elif mmi == 3:
        print ("Loading...")
        pbar()
    elif mmi == 4:
        print ("Logging out...")
        #shtdwn() | Shutdown class is currently not implmented
        sys.exit()
    elif mmi == 5:
        print ("Loading...")
        settings()

def settings(): #Settings menu, but no settings
    main_menu() #Goes back to main menu until theres funticans

def shtdwn(): #Log out process to close data logging and save to local FS and network

main()
