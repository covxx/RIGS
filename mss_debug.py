# RIGS | RPi Indoor Grow Sensor System
# https://github.com/covxx/mss
# Build Date 3/21/2023
# Build Ver. 0.5
#from signal import pause
import subprocess
import math
import threading
import sys
import select
import time
import os
from os import system
from datetime import datetime
from datetime import date
from os import system, name
#import exists
from sense_hat import SenseHat
#from prometheus_client import Gauge, start_http_server #For web server
#web_port = 9090 #Web server port
#start_http_server(web_port) #Web sever start
#gt = Gauge('RIGS_temperature',
#           'Temperature measured by the RIGS Sensor', ['scale'])
sense = SenseHat()
sense.clear()
today_date = date.today()
current_date = today_date.strftime("%m_%d_%Y") #Gets date, saves to var
today_date_time = datetime.now()
current_date_time = today_date_time.strftime("%m/%d/%Y %I:%M%p") #Gets date and time and saves to var in 12 hour format
def clear_screen():
    if name == 'nt': #Clear screen for windows
        _ = system('cls')
    else: #Clear screen for Mac and Linux
        _ = system('clear')
def FRun(): #First time run check check, verifies config file is present
	config_exists = os.path.exists('config.txt') 
	if config_exists == True:
		print(config_exists) #Debug
		MainStart()
	if config_exists == False:
		ConfigSetup() #Calls program config
		#print(config_exists) #Debug
def ConfigSetup(): #Creates config file
	clear_screen()
	print('Welcome to RIGS')
	print('Please wait, preforming first time setup...')
	with open('config.py', 'w'): pass
	MainStart()
def MainStart():
	clear_screen()
	print('Welcome to RIGS')
	print ('Today is', current_date_time)
	print('----------------------------------------------')
	print('1. Start Data Logging')#Run data logging session
	print("2. Sensor Data") #Live Data From Sensors
	#print("3. Settings") #Settings - TBD if needed
	print('4. Exit') #Close Program
	print ('----------------------------------------------')
	msi = int(input('Enter number selection to proceed:  '))
	if msi == 1:
		print ("Loading...")
		Start_DLS() #| In Progress... 
	elif msi == 2:
		print ("Loading...")
		#sm()
	elif msi == 3:
		print ("Loading...")
    	#setng()
	elif msi == 4: 
		print ("Shuting down application")
		exit() #Closes program
	else:
		MainStart()
def Start_DLS(): #General Datalogging, will become menu later with abilty to define args, now for debuging
	clear_screen()
	dls_temp = 0 #Current temp
	LogCount = 0 #Loop timer
	LogTime = 0
	LogTime = int(input('How many seconds do you want to datalog for?:	'))
	LogRemain = LogTime #Time remaining counter
	while (LogCount < LogTime):
		LogCount = LogCount + 1
		LogRemain = LogRemain - 1
		clear_screen()
		real_temp = sense.get_temperature() #Gets temp from sensehat
		DLS_FileName = ('Temp_Log_' + str(current_date) + '.txt') #Sets log file namee using 'todays' date from var current_date
		with open(DLS_FileName, "a") as f: #Append data if file exists but will create new if not
			f.write( str(current_date_time) + ': The current tempture is: ' + str(real_temp) + ' F \n') #Writes current temp to new line
			print('Data logging in progress: ' + str(LogRemain) + (' seconds remaining in session.')) #Prints seconds left of DLS session
			time.sleep(0.5) #Waits half second before looping
	clear_screen()
	print('Data logging session has completed, log saved as ' + DLS_FileName )
	input('Press enter to return to main menu.')
	MainStart()
clear_screen()
FRun()