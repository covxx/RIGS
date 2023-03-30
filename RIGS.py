# RIGS | RPi Indoor Grow Sensor System
# https://github.com/covxx/mss
# Build Date 3/30/2023
# Build Ver. 0.6
import os
import time
import logging
import cursor
from threading import * #Needed for GUL + program to run at same time
from os import system
from datetime import datetime
from datetime import date
from os import system, name
from tkinter import simpledialog, Tk, Canvas, Entry, Text, PhotoImage, Button, messagebox
from pathlib import Path
global comp_usage
global GUI
global Auto_TotalRun_Counter
global Auto_LogCount
global Auto_LogTime
global Auto_LogInterval
global b_ver
global Auto_LogCount_save
global Auto_LogInterval_Switch
global Prog_TRun
global Prog_TRun_M
global breaker 
breaker = 1 #Please break all loops
Auto_LogInterval_Switch = 0 #DEBUG DEBUG 
b_ver = ("v0.5 3_30_2023") #Bulid verison, used for GUI
Prog_TRun = 0 #Program total run time (used for threading and progress bar TBD)
Prog_TRun_M = 0 #Program total in minutes instead
comp_usage = "Palumbo Foods LLC" #Company using
Auto_LogCount_save = 0 #Place holder var used for automated data logging
Auto_TotalRun_Counter = 0 #Place holder var used for automated data logging
Auto_LogTime = 0 #Logtime for automated logging, user will need to set 
Auto_LogTime_counter = Auto_LogTime #Counter for logging, able to be reset and preserve data
Auto_LogInterval = 0 #How long till data logging starts
Auto_LogInterval_Counter = Auto_LogInterval #counter
Auto_LogCount = 0 #Place holder var used for automated data logging
today_date = date.today() #Sets todays date as the current date
current_date = today_date.strftime("%m_%d_%Y") #Gets date, saves to var
today_date_time = datetime.now() #Gets date and time, var
current_date_time = today_date_time.strftime("%m/%d/%Y %I:%M%p") #Gets date and time and saves to var in 12 hour format
current_time = today_date_time.strftime("%I:%M%p")
cursor.hide() #Does what it says
if os.environ.get('DISPLAY','') == '': #DEBUG for SSH testing
    #print('no display found. Using :0.0') #DEBUG for SSH testing
    os.environ.__setitem__('DISPLAY', ':0.0') #DEBUG for SSH testing
def Thread_ADLS(): #Auto_Data_Logging thread call, so tkinter window and code run | IN PROGRESS
	t1=Thread(target=Auto_DLS_Start_prog)
	t1.start()
def clear_screen(): #Cross platform screen clearing
    if name == 'nt': #Clear screen for windows
        _ = system('cls')
    else: #Clear screen for unix
        _ = system('clear')
def FRun(): #First time run check check, verifies config file is present
	config_exists = os.path.exists('config.txt') 
	if config_exists == True:
		print(config_exists) #Debug
		MainStart()
	if config_exists == False:
		ConfigSetup() #Calls program config
		#print(config_exists) #Debug
def ConfigSetup(): #Creates config file |
	clear_screen()
	print('Welcome to RIGS') #MSG BOX NEEDED
	print('Please wait, preforming first time setup...') #MSG BOX NEEDED
	with open('config.txt', 'w'): pass
	time.sleep(3)
	MainStart()
def Main_Menu_B(): #Returns to main menu
	clear_screen()
	window.deiconify() #Shows main window again
def MainStart():
	clear_screen()
	print('Welcome to RIGS')
	print ('Today is', current_date_time, " | ", b_ver)
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
		#Start_DLS() #Data logging to log file works, need to figure out sensor situation to implemnent actual data instead of static var
	elif msi == 2:
		print ("Loading...")
		Auto_DLS_PreStart()
	elif msi == 3:
		print ("Loading...")
		Start_man_DLS()
	elif msi == 4: 
		print ("Shuting down application")
		exit() #Closes program
	else:
		MainStart()
def Auto_LogCheck(): #Sets log interval to 0 seconds if there is only one test
	global Auto_LogCount
	global Auto_LogInterval_Counter
	global Auto_LogInterval_Switch
	if Auto_LogCount == 1:
		Auto_LogInterval_Switch = 0
		#print(Auto_LogInterval) #DEBUG
		#time.sleep(3) #DEBUG
		return
	else: #Nothing to change
		Auto_LogInterval_Switch = 1
		return
def Auto_DLS_PreStart(): #Need to set variables first - could use lists instead
	global window
	global Auto_LogCount 
	global Auto_LogTime
	global Auto_LogInterval
	global Auto_LogTime_counter
	global Auto_LogInterval_Counter
	global Auto_LogCount_save #Saving log count for times around the sun
	global Auto_dls_temp #Temp place holder 
	global Prog_TRun #Total program run time
	global Prog_TRun_M #Total program run time in minutes 
	Auto_dls_temp = 1
	clear_screen()
	window.withdraw() #Closes Tkinter window
	Auto_LogTime = simpledialog.askinteger(title="RIGS Automated Testing",
				       							prompt="How Long would you like to data log for, in minutes? ")
	Auto_LogCount = simpledialog.askinteger(title="RIGS Automated Testing",
				       							prompt="Enter how many times would you like to data log? ")
	Auto_LogInterval = simpledialog.askinteger(title="RIGS Automated Testing", #Would like to remove this if not needed but will assume multi sessions for now.
					       							prompt="Enter how long between data logging sessions, in minutes? ")
	#print(Auto_LogInterval)
	#time.sleep(3)
	Auto_LogTime_counter = Auto_LogTime_counter + (Auto_LogTime * 60) #Counter for logging, able to be reset and preserve data
	Auto_LogInterval_Counter = Auto_LogInterval_Counter + (Auto_LogInterval * 60) #counter DEBUG DEBUG DEBUG UNCOMMENT ^^
	Auto_LogCheck() #DEBUG DEBUG = Need to adjust automated function to keep running when this runs
	#time.sleep(3) #More DEBUG comments
	#print(Auto_LogInterval_Counter) #DEBUG
	#time.sleep(3) #DEBUG
	Prog_TRun = Prog_TRun + ((Auto_LogTime_counter + Auto_LogInterval_Counter) * Auto_LogCount)
	Prog_TRun_M = (Prog_TRun // 60) #Convert total run time to minutes
	Auto_LogCount_save = (Auto_LogCount_save + Auto_LogCount)
	DLS_FileName = ('Temp_Log_' + str(current_date) + '.txt') #Adds session details to file
	with open(DLS_FileName, "a") as f: #Append data if file exists but will create new if not
			f.write("** New data logging session start at " + str(current_time) + ' : Each test will run for: ' + str(Auto_LogTime) + ' minute(s). Test(s) will run ' + str(Auto_LogInterval) + ' seconds after the last. Total amount of tests to run is ' + str(Auto_LogCount) + ' ** \n') #Writes sessions details before session starts
	Auto_DLS_Start() #Lets go
def Auto_DLS_Start(): #Automated DLS, vars from Auto_DLS_PreStart
	window.withdraw() #Removes main window
	clear_screen() #DEBUG
	print("DEBUG 7") #DEBUG DEBUG
	#Thread_ADLS() #DEBUG DEBUG WORKS!
	print("DEBUG 8") #DEBUG DEBUG
	global Auto_LogCount #How many tests to run
	global Auto_LogTime #How long tests run for
	global Auto_LogInterval #How long inbetween tests
	global Auto_LogTime_counter
	global Auto_LogInterval_Counter
	global Auto_LogCount_save
	global Auto_dls_temp
	global Prog_TRun
	global Auto_LogInterval_Switch
	Auto_dls_temp = 5 #Var for temp, auto hold
	Auto_DLS_Start_prog()
def Auto_DLS_Start_prog(): #Function for DLS, needed to seperate for threading on window **CURRENT TESTING**
	clear_screen()
	global Auto_LogCount #How many tests to run
	global Auto_LogTime #How long tests run for
	global Auto_LogInterval #How long inbetween tests
	global Auto_LogTime_counter
	global Auto_LogInterval_Counter
	global Auto_LogCount_save
	global Auto_dls_temp
	global Prog_TRun
	global Prog_TRun_M
	global breaker
	messagebox.showinfo("RIGs - In Progress PLEASE WAIT","Data logging session in progress, please wait.  Total log time is " + str(Prog_TRun_M) + " minute(s)")
	while (Auto_LogTime_counter != 0 and Auto_LogInterval_Counter != 0):
		clear_screen()
		DLS_FileName = ('logs\Temp_Log_' + str(current_date) + '.txt') #Sets log file name using 'todays' date from var current_date
		with open(DLS_FileName, "a") as f: #Append data if file exists but will create new if not
			f.write( str(current_time) + ': The current tempture is: ' + str(Auto_dls_temp) + '  F \n') #Writes current temp to new line with time
			print(current_date_time + ': The current tempture is: ' + str(Auto_dls_temp) + 'F') #Prints current date and time with tempture
			print('Data logging in progress: ' + str(Auto_LogTime_counter) + (' seconds remaining in session.')) #Prints seconds left of DLS session
		time.sleep(1.0) #Wait for timer loop
		Auto_LogTime_counter = (Auto_LogTime_counter - 1)
		while (Auto_LogTime_counter == 0 and Auto_LogInterval_Counter > 0):
			clear_screen()
			if Auto_LogInterval_Switch == 0:
				#Auto_LogCount = 0
				clear_screen()
				print("All testing has completed, software has ran ", Auto_LogCount_save, "tests. For a complete run time of", Prog_TRun,"seconds.")
				print('Data logging session has completed, log saved as ' + DLS_FileName )
				messagebox.showinfo("RIGS","Data logging session has finished. Total log time is " + str(Prog_TRun_M) + " minute(s). Data log file named, " + DLS_FileName)
				time.sleep(5)
				window.deiconify() #Shows main window again
				Main_Menu_B()
				breaker = 1
				break
			if Auto_LogInterval_Switch == 1:
				print("Automated data logging session has finished, next session starts in ", Auto_LogInterval_Counter, " seconds.")
				Auto_LogInterval_Counter = (Auto_LogInterval_Counter - 1)
				time.sleep(1.0) #Wait for timer loop
			if Auto_LogCount == 0: #No more testing
				clear_screen()
				print("All testing has completed, software has ran ", Auto_LogCount_save, "tests. For a complete run time of", Prog_TRun,"seconds.")
				print('Data logging session has completed, log saved as ' + DLS_FileName )
				messagebox.showinfo("RIGS","Data logging session has finished. Total log time is " + str(Prog_TRun_M) + " minute(s). Data log file named, " + DLS_FileName)
				time.sleep(3)
				Main_Menu_B()
				breaker = 1
				break
			if Auto_LogTime_counter == 0 and Auto_LogInterval_Counter == 0:
				Auto_LogCount = Auto_LogCount - 1 #Minus 1 to log count	| Auto_LogTime_counter = Auto_LogTime_counter + Auto_LogTime
				Auto_LogTime_counter = Auto_LogTime_counter + (Auto_LogTime * 60) #Counter for logging, able to be reset and preserve data
				Auto_LogInterval_Counter = Auto_LogInterval_Counter + (Auto_LogInterval * 60)
				print("DEBUG 13")
				print(Auto_LogCount)
				print(Auto_LogTime_counter)
				print(Auto_LogInterval_Counter)
				time.sleep(3)
				Auto_DLS_Start_prog()
def Start_man_DLS(): #Live sensor data menu, no logging | IN PROGRESS
	window.withdraw() #Removes main window
	global Man_dls_temp #
	Man_DLS_Log = 1
	Man_dls_temp = 0 #place holder for actual temp
	clear_screen()
	try:
		while Man_DLS_Log != 0:
			clear_screen()
			print("Sensor data will be shown below, to exit press CTRL+C.")
			print(current_date_time + ': The current tempture is: ' + str(Man_dls_temp) + 'F') #Prints current date and time with tempture, loops till CTRL+C 
			Man_DLS_Log = Man_DLS_Log + 1
			Man_dls_temp = Man_dls_temp + 1
			time.sleep(1.0) #Matrix wall without
	except KeyboardInterrupt:
		clear_screen()
		print('The final tempture is: ', Man_dls_temp, 'F')
		print("Session has been ended, returning to main menu..")
		time.sleep(3.0) #Sleep for message to display, yes making it slower on purpose
		window.deiconify() #Brings main window back
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:/Users/JENS3/Desktop/RIGS/assets/frame0")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
window = Tk()
window.title("RIGS - Automated Data Logging") #GUI Window Name
if "nt" == os.name: #Cross platform bitmaps
    window.wm_iconbitmap(bitmap = r"C:/Users/JENS3/Desktop/RIGS/assets/rigs.ico") #Need to be relative
else:
    window.wm_iconbitmap(bitmap = r'C:/Users/JENS3/Desktop/RIGS/assets/@rigs.xbm') #Need to be relative
window.geometry("469x408")
window.configure(bg = "#FFFFFF")
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 408,
    width = 469,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    234.0,
    102.0,
    image=image_image_1
)
canvas.create_text(
    130.0,
    390.0,
    anchor="nw",
    text="Licensed for: " + comp_usage,
    fill="#000000",
    font=("Inter", 12 * -1)
)
canvas.create_text(
    143.0,
    378.0,
    anchor="nw",
    text="Copyright 2023 Christian Jensen", #"Licensed for: " + comp_usage,
    fill="#000000",
    font=("Inter", 12 * -1)
)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Start_man_DLS(), #print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=35.0,
    y=166.0,
    width=96.0,
    height=23.0
)
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Auto_DLS_PreStart(), #print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=177.0,
    y=166.0,
    width=115.0,
    height=23.0
)
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=337.0,
    y=166.0,
    width=96.0,
    height=23.0
)
button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=180.0,
    y=216.0,
    width=96.0,
    height=23.0
)
button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: exit(), #Goodbye :(
    relief="flat"
)
button_5.place(
    x=180.0,
    y=260.0,
    width=96.0,
    height=23.0
)
canvas.create_text(
    139.0,
    36.0,
    anchor="nw",
    text="Automated data logging software",
    fill="#000000",
    font=("Inter", 12 * -1)
)
canvas.create_text(
    5.0,
    9.0,
    anchor="nw",
    text=b_ver,
    fill="#000000",
    font=("Inter", 12 * -1)
)
canvas.create_text(
    220.0,
    20.0,
    anchor="nw",
    text="RIGS",
    fill="#000000",
    font=("Inter", 12 * -1)
)
canvas.create_rectangle(
    118.0,
    53.0,
    348.0,
    54.0,
    fill="#000000",
    outline="")
window.resizable(False, False)
window.mainloop()
clear_screen()