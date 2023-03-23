# RIGS | RPi Indoor Grow Sensor System
# https://github.com/covxx/mss
# Build Date 3/22/2023
# Build Ver. 0.5
import os
import time
import logging
from os import system
from datetime import datetime
from datetime import date
from os import system, name
Auto_LogTime = 0 #Logtime for automated logging, user will need to set 
Auto_LogTime_counter = Auto_LogTime #Counter for logging, able to be reset and preserve data
Auto_LogInterval = 0 #How long till data logging starts
Auto_LogInterval_Counter = Auto_LogInterval #counter
Auto_LogCount = 0
today_date = date.today() #Sets todays date as the current date
current_date = today_date.strftime("%m_%d_%Y") #Gets date, saves to var
today_date_time = datetime.now()
current_date_time = today_date_time.strftime("%m/%d/%Y %I:%M%p") #Gets date and time and saves to var in 12 hour format
current_time = today_date_time.strftime("%I:%M%p")
from prometheus_client import Gauge, start_http_server #For web server
web_port = 9090 #Web server port
start_http_server(web_port) #Web sever start
gt = Gauge('RIGS_temperature',
           'Temperature measured by the RIGS Sensor', ['scale'])
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
	with open('config.txt', 'w'): pass
	MainStart()
def MainStart():
	clear_screen()
	print('Welcome to RIGS')
	print ('Today is', current_date_time)
	print('----------------------------------------------')
	print('1. Start Data Logging')#Run data logging session
	print("2. Automated data logging") #Live Data From Sensors
	print("3. Live Sensor Data") #Live Data From Sensors
	#print("3. Settings") #Settings - TBD if needed
	print('4. Exit') #Close Program
	print ('----------------------------------------------')
	msi = int(input('Enter number selection to proceed:  '))
	if msi == 1:
		print ("Loading...")
		Start_DLS() #Data logging to log file works, need to figure out sensor situation to implemnent actual data instead of static var
	elif msi == 2:
		print ("Loading...")
		Auto_DLS_PreStart()
	elif msi == 3:
		print ("Loading...")
		Start_sd()
	elif msi == 4: 
		print ("Shuting down application")
		exit() #Closes program
	else:
		MainStart()
def Auto_DLS_PreStart(): #Need to set variables first - could use lists instead
	clear_screen()
	print('RIGS Automated Data logging Setup')
	print('------------------------------------')
	Auto_LogTime = input('Enter how long would you like to data log for? (in seconds): ')
	Auto_LogCount = input('Enter how many times would you like to data log? (1-10): ')
	Auto_LogInterval = input("Enter how long between data logging sessions, in seconds?: ")
	print(Auto_LogTime)
	print(Auto_LogCount)
	print(Auto_LogInterval)
	()
def Auto_DLS_Start(): #Automated DLS, vars from Auto_DLS_PreStart
	#clear_screen()
	Auto_dls_temp = 0 #Var for temp, auto hold
	Auto_LogTime_counter = Auto_LogTime #Counter for logging, able to be reset and preserve data
	Auto_LogInterval_Counter = Auto_LogInterval #counter
	while Auto_LogTime_counter > 0:
		Auto_LogTime_counter = Auto_LogTime_counter - 1
		DLS_FileName = ('Temp_Log_' + str(current_date) + '.txt') #Sets log file namee using 'todays' date from var current_date
		with open(DLS_FileName, "a") as f: #Append data if file exists but will create new if not
			f.write( str(current_time) + ': The current tempture is: ' + str(Auto_dls_temp) + ' F \n') #Writes current temp to new line with time
			print('Data logging in progress: ' + str(Auto_LogTime_counter) + (' seconds remaining in session.')) #Prints seconds left of DLS session
			time.sleep(0.5) #Waits half second before looping
		if Auto_LogTime_counter == 0: #Once session has finished	
			Auto_LogCount = Auto_LogCount - 1 #Minus 1 to log count
			Auto_LogTime_counter = Auto_LogTime_counter + Auto_LogTime
			while Auto_LogCount != 0 and Auto_LogInterval_Counter != 0:
				#clear_screen()
				print(str(Auto_LogInterval_Counter))
				Auto_LogInterval_Counter = Auto_LogInterval_Counter - 1
				print("Automated data logging session has finished, next session starts in ", Auto_LogInterval_Counter, " seconds.")
				time.sleep(2.0) #Wait
			if Auto_LogInterval_Counter == 0:
				Auto_DLS_Start()
			if Auto_LogCount == 0:
				#clear_screen()
				print("Automated data logging session has finished")
				print(str(Auto_LogCount)) #Debug
				print(str(Auto_LogInterval)) #Debug
				time.sleep(40) #DEBUGGG
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
		DLS_FileName = ('Temp_Log_' + str(current_date) + '.txt') #Sets log file namee using 'todays' date from var current_date
		with open(DLS_FileName, "a") as f: #Append data if file exists but will create new if not
			f.write( str(current_time) + ': The current tempture is: ' + str(dls_temp) + ' F \n') #Writes current temp to new line with time
			print('Data logging in progress: ' + str(LogRemain) + (' seconds remaining in session.')) #Prints seconds left of DLS session
			time.sleep(0.5) #Waits half second before looping
	clear_screen()
	print('Data logging session has completed, log saved as ' + DLS_FileName )
	input('Press enter to return to main menu.')
	MainStart()
def Start_sd(): #Live sensor data menu, no logging | IN PROGRESS
	sd_temp = 0
	clear_screen()
	try:
		while True:
			clear_screen()
			print("Sensor data will be shown below, to exit press CTRL+C.")
			print(current_date_time, ': The current tempture is: ', sd_temp) #Prints current date and time with tempture, loops till CTRL+C
			time.sleep(1.0) #Matrix wall without
	except KeyboardInterrupt:
			clear_screen()
			print('The final tempture is: ', sd_temp, 'F')
			print("Session has been ended, returning to main menu..")
			time.sleep(3.0) #Sleep for message to display, yes making it slower on purpose
			MainStart() #Back to menu
clear_screen()
FRun()