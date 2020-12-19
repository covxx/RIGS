#MSS 2021 Rewritten // V0.1
# Copyright Christian Jensen @covxx
# Contact cmjensenx@gmail.com
import os
import os.path
from pathlib import Path
#Sense hat functions removed for testing with Win10
#from sense_hat import SenseHat
#sense = SenseHat()
setf = Path("config.ini") #Path For Config File
arun = 'F' #var for first time check, gets over written by ftrun()
def clear_S(): #Call back for screen clearing
    os.system('cls')
def ftrun(): #First time run check
    setf = Path("config.ini")
    if setf.is_file(): #checks if file exists
        global arun
        arun = "True"
        #print(arun) #Debug for first time check
        main_Menu() #Runs main menu
    else:
        ftsetup() #Runs first time setup
def ftsetup(): #First time setup config //In Progress
    clear_S()
    f= open('config.txt',"w+") #Creates config file
    arun = "True"
    print(arun)
    main_Menu()
def main_Menu():
    clear_S()
    #print(arun) #Debug for first time check
    print ("Welcome to Robin Farming Intrustment")
    print ("Alpha Ver. 0.1 - 12/20")
    print ("----------------------------------------------")
    print("1. Start Data Logging") #Run data logging session
    print ("2. Sensor Data") #Sub menu with sensor specific test
    print ("3. Settings") #Program settings
    print ("4. Shut Down") #Close Program
    print ("----------------------------------------------")
    # MMI = Main Menu Input
    mmi = int(input("Enter number selection to proceed:  "))
    #print(mmi) # Test EOF
    if mmi == 1:
        print ("Loading...")
        #start_dls() | Not implemented
    elif mmi == 2:
        print ("Loading...")
        sm()
    elif mmi == 3:
        print ("Loading...")
        #settings() | | Not implemented
    elif mmi == 4: #May need to create a end prog function
        clear_S()
        print ("Good Bye")
        exit() #Closes program
def sm(): #Menu Option Two
    clear_S()
    print ("Manual Data Logging Menu")
    print ("1. Temperature") #Prints Temp
    print ("2. Humidity") #Print Humidity
    print ("3. Pressure") #Prints Pressure
    print ("4. Main Menu")
    print ("----------------------------------------------")
    smi = int(input("Enter number selection to proceed:  "))
    if smi == 1:
        print ("Loading...")
        #get_temp() | Not implemented
    elif smi == 2:
        print ("Loading...")
        #hum() | Not implemented
    elif smi == 3:
        print ("Loading...")
        #pbar() | Not implemented
    elif smi == 4:
        print("Loading main menu..")
        main_Menu()
#def start_dls(): #Data Logging start, loads config file to start
ftrun() #Check for first time setup
#main_Menu() #Starts Program
