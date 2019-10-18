#Main program for MSS
# Copy right Christian Jensen @covxx
# Contact cmjensenx@gmail.com
#
import sys
from sense_hat import SenseHat
import datetime
import glob
from sense_hat import SenseHat
#Configuring sensehat
sense = SenseHat()
sense.clear()
temp = round(sense.get_temperature()*9/5+32)
humi = round(sense.get_humidity())
mbar = round(sense.get_pressure())
#All other program setup
tf = open('TempLog.txt', 'a')
ctime = datetime.datetime.now()
def get_temp(): #Prints temp and is EOP
    print ("The temperature is currently:" ,temp, "F")
 #   tf.write(sense.temp)
  #  tf.write('\n')
   # tf.writeclose()
    #sleep(50)
def hum():
     print ("The humidity is currently:",humi, "%")
     
def pbar():
    print ("The pressure is currently:",mbar,"mbar")

def main_Menu():
    print ("Welcome to Robin Farming Intrustment")
    print ("Ver. 0.1.0")
   # print ("The time currently is:"), ctime.strftime("%Y-%M-%D %H:%m:s")
    print ("----------------------------------------------")
    print ("1. Temperature") # Prints Temp
    print ("2. Humidity") #Print Humidity
    print ("3. Pressure") # Pressure
    print ("3. Quit") # Close Program
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
    elif mmi == 4:
        print ("Goodbye")
        sys.exit()
    elif mmi == 3:
        print ("Loading...")
        pbar()
            
main_Menu() #runs the program