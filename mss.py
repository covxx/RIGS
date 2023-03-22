# RIGS | RPi Indoor Grow Sensor System
# https://github.com/covxx/mss
# Build Date 09/15/2022 
# Build Ver. 0.1
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
#import os.name
#import exists
#from sense_hat import SenseHat
today_date = datetime.now()
current_date = today_date.strftime("%d/%m/%Y %H:%M:%S") #Gets date and saves to var
today_date_time = datetime.now()
current_date_time = today_date_time.strftime("%d/%m/%Y %H:%M:%S") #Gets date and time and saves to var
def cls():
	system('clear')
def FRun(): #First time run check check, verifies config file is present
	config_exists = os.path.exists('config.txt') 
	if config_exists == True:
		print(config_exists) #Debug
		MainStart()
	if config_exists == False:
		ConfigSetup() #Calls program config
		#print(config_exists) #Debug
def ConfigSetup(): #Creates config file
	cls()
	print('Welcome to RIGS')
	print('Please wait, preforming first time setup...')
	with open('config.py', 'w'): pass
	MainStart()
def MainStart():
	cls()
	print('Welcome to RIGS')
	print ('Today is', current_date)
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
	cls()
	current_temp = 0 #Current temp
	LogCount = 0 #Loop timer
	LogTime = 0
	LogTime = int(input('How many seconds do you want to datalog for?:	'))
	while (LogCount < LogTime):   
		LogCount = LogCount + 1
		cls()
		with open('test.txt', "w+"): #Will need to be set to current date
			with open.write('Tempture is', current_temp):
				time.sleep(1) #Waits a second before looping, need to make a better way to do this.
	print(LogCount)
cls()
FRun()