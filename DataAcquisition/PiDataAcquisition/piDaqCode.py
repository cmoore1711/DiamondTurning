# Start Imports


# Global Imports

import Adafruit_GPIO
import RPi.GPIO as GPIO
import time
import Adafruit_ADS1x15
import mysql.connector
import socket

# Local Imports
from Adafruit_MAX31856 import MAX31856 as MAX31856
# End Imports


# Begin Setup
#edit the text file, not these lines!

def cToF(tempinC):
    return (tempinC*1.8)+32


successfulSetup = False
while(successfulSetup ==False):
    try:
            

        path = '/home/pi/Desktop/deviceInfo.txt'
        deviceInfoFile = open(path,'r')
        unusedLine = deviceInfoFile.readline().rstrip('\n')
        machineName = deviceInfoFile.readline().rstrip('\n')

        unusedLine = deviceInfoFile.readline().rstrip('\n')
        deviceName = deviceInfoFile.readline().rstrip('\n')

        unusedLine = deviceInfoFile.readline().rstrip('\n')
        department = deviceInfoFile.readline().rstrip('\n')

        unusedLine = deviceInfoFile.readline().rstrip('\n')
        queryInterval = deviceInfoFile.readline().rstrip('\n')
        queryInterval = int(queryInterval)

        unusedLine = deviceInfoFile.readline().rstrip('\n')
        useSensors = deviceInfoFile.readline().rstrip('\n')

        unusedLine = deviceInfoFile.readline().rstrip('\n')
        isUtilizationDevice = deviceInfoFile.readline().rstrip('\n')

        unusedLine = deviceInfoFile.readline().rstrip('\n')
        isLogicalUtil = deviceInfoFile.readline().rstrip('\n')

        unusedLine = deviceInfoFile.readline().rstrip('\n')
        logicIfIsUtil = deviceInfoFile.readline().rstrip('\n')


        unusedLine = deviceInfoFile.readline().rstrip('\n')
        isUtilizationONLY = deviceInfoFile.readline().rstrip('\n')

        m1=m2=m3=m4=1
        b1=b2=b3=b4=0
        #mx+b

        t1=t2=t3=t4='K'
        u1=u2=u3=u4='F'
        #thermocouple type
        #units (F or C)

        unusedLine = deviceInfoFile.readline().rstrip('\n')
        numAnalog = deviceInfoFile.readline().rstrip('\n')
        numAnalog = int(numAnalog)
        if(numAnalog>0):
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            m1 = deviceInfoFile.readline().rstrip('\n')
            m1 = float(m1)
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            b1 = deviceInfoFile.readline().rstrip('\n')
            b1 = float(b1)
        if(numAnalog>1):
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            m2 = deviceInfoFile.readline().rstrip('\n')
            m2 = float(m2)
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            b2 = deviceInfoFile.readline().rstrip('\n')
            b2 = float(b2)
        if(numAnalog>2):
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            m3 = deviceInfoFile.readline().rstrip('\n')
            m3 = float(m3)
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            b3 = deviceInfoFile.readline().rstrip('\n')
            b3 = float(b3)
        if(numAnalog>3):
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            m4 = deviceInfoFile.readline().rstrip('\n')
            m4 = float(m4)
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            b4 = deviceInfoFile.readline().rstrip('\n')
            b4 = float(b4)

            
        unusedLine = deviceInfoFile.readline().rstrip('\n')
        numThermocouple = deviceInfoFile.readline().rstrip('\n')
        numThermocouple = int(numThermocouple)


        if(numThermocouple>0):
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            t1 = deviceInfoFile.readline().rstrip('\n')   
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            u1 = deviceInfoFile.readline().rstrip('\n')
        if(numThermocouple>1):
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            t2 = deviceInfoFile.readline().rstrip('\n')    
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            u2 = deviceInfoFile.readline().rstrip('\n')    
        if(numThermocouple>2):
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            t3 = deviceInfoFile.readline().rstrip('\n')   
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            u3 = deviceInfoFile.readline().rstrip('\n') 
        if(numThermocouple>3):
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            t4 = deviceInfoFile.readline().rstrip('\n')
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            u4 = deviceInfoFile.readline().rstrip('\n')
            


        print("Query interval: " + str(queryInterval) + " seconds")

        print("Machine Name: " + machineName)
        print("Device Name: " + deviceName)


        GPIO.setmode(GPIO.BCM)
        # uses BCM mode rather than Board mode (use GPIO numbering of pins not board numbering)

        GAIN = 1
        # Sets analog gain value





        # Set BCM Pins if sensors exist in general
        #High on 25 to let you know the code is running 
        #GPIO.setup(25, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(21, GPIO.OUT)
        GPIO.setup(20, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)
        GPIO.setup(12, GPIO.OUT)

        # BCM pins 4 17 27 22 are for Digital I/O, and all are pulled down.
        #5/15/2018 CBM All digital pins are on by default!
        ####

        GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        # BCM pins 2 and 3  are for Analog I/O.
        # 2 3 are for hardware I2C
        # All are scaled to 0-5V at a 12-bit resolution

        # VDD to Raspberry Pi 5V, GND to Raspberry Pi GND, SCL to Raspberry Pi SCL, SDA to Raspberry Pi SDA
        # or create an ADS1115 ADC (16-bit) instance depending upon sensor
        # adc = Adafruit_ADS1x15.ADS1115()

        # BCM pins 0 5 6 19 are for Thermocouples
        # Pins 0 5 6 19 are for the CS inputs of the thermocouples
        # Pins 10 9 11 are MOSI(SDO), MISO(SDI), and SCLK respectively

        # Raspberry Pi software SPI configuration.
        # software_spi = {"clk": 25, "cs": 8, "do": 9, "di": 10}
        # sensor = MAX31856(software_spi=software_spi)
        # End Setup
        successfulSetup = True
    except:
        print("Unsuccessful setup.")
print("Setup Successful")

while(True):
    try:
        
        path = '/home/pi/Desktop/deviceInfo.txt'
        deviceInfoFile = open(path,'r')
        unusedLine = deviceInfoFile.readline().rstrip('\n')
        machineName = deviceInfoFile.readline().rstrip('\n')

        unusedLine = deviceInfoFile.readline().rstrip('\n')
        deviceName = deviceInfoFile.readline().rstrip('\n')

        unusedLine = deviceInfoFile.readline().rstrip('\n')
        department = deviceInfoFile.readline().rstrip('\n')

        unusedLine = deviceInfoFile.readline().rstrip('\n')
        queryInterval = deviceInfoFile.readline().rstrip('\n')
        queryInterval = int(queryInterval)

        unusedLine = deviceInfoFile.readline().rstrip('\n')
        useSensors = deviceInfoFile.readline().rstrip('\n')

        unusedLine = deviceInfoFile.readline().rstrip('\n')
        isUtilizationDevice = deviceInfoFile.readline().rstrip('\n')

        unusedLine = deviceInfoFile.readline().rstrip('\n')
        isLogicalUtil = deviceInfoFile.readline().rstrip('\n')

        unusedLine = deviceInfoFile.readline().rstrip('\n')
        logicIfIsUtil = deviceInfoFile.readline().rstrip('\n')


        unusedLine = deviceInfoFile.readline().rstrip('\n')
        isUtilizationONLY = deviceInfoFile.readline().rstrip('\n')
        if(isUtilizationONLY== 'Y'):
            GPIO.output(20, GPIO.LOW) 
        m1=m2=m3=m4=1
        b1=b2=b3=b4=0
        #mx+b

        t1=t2=t3=t4='K'
        u1=u2=u3=u4='F'
        #thermocouple type
        #units (F or C)

        unusedLine = deviceInfoFile.readline().rstrip('\n')
        numAnalog = deviceInfoFile.readline().rstrip('\n')
        numAnalog = int(numAnalog)
        if(numAnalog>0):
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            m1 = deviceInfoFile.readline().rstrip('\n')
            m1 = float(m1)
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            b1 = deviceInfoFile.readline().rstrip('\n')
            b1 = float(b1)
        if(numAnalog>1):
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            m2 = deviceInfoFile.readline().rstrip('\n')
            m2 = float(m2)
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            b2 = deviceInfoFile.readline().rstrip('\n')
            b2 = float(b2)
        if(numAnalog>2):
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            m3 = deviceInfoFile.readline().rstrip('\n')
            m3 = float(m3)
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            b3 = deviceInfoFile.readline().rstrip('\n')
            b3 = float(b3)
        if(numAnalog>3):
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            m4 = deviceInfoFile.readline().rstrip('\n')
            m4 = float(m4)
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            b4 = deviceInfoFile.readline().rstrip('\n')
            b4 = float(b4)

            
        unusedLine = deviceInfoFile.readline().rstrip('\n')
        numThermocouple = deviceInfoFile.readline().rstrip('\n')
        numThermocouple = int(numThermocouple)


        if(numThermocouple>0):
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            t1 = deviceInfoFile.readline().rstrip('\n')   
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            u1 = deviceInfoFile.readline().rstrip('\n')
        if(numThermocouple>1):
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            t2 = deviceInfoFile.readline().rstrip('\n')    
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            u2 = deviceInfoFile.readline().rstrip('\n')    
        if(numThermocouple>2):
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            t3 = deviceInfoFile.readline().rstrip('\n')   
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            u3 = deviceInfoFile.readline().rstrip('\n') 
        if(numThermocouple>3):
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            t4 = deviceInfoFile.readline().rstrip('\n')
            unusedLine = deviceInfoFile.readline().rstrip('\n')
            u4 = deviceInfoFile.readline().rstrip('\n')


        print("Query interval: " + str(queryInterval) + " seconds")

        print("Machine Name: " + machineName)
        print("Device Name: " + deviceName)



        
        # loop indefinitely
        try:
            cursor.close()
        except:
            print('No open cursor')
        try:
            cnx.close()
        except:
            print('No open CNX')
        cnx = mysql.connector.connect(user='daq', password='dataacquisition',host='10.10.9.107')
        cursor = cnx.cursor()
        for blinkloop in range(10):
            GPIO.output(21, GPIO.LOW)
            time.sleep(queryInterval/50)
            GPIO.output(21, GPIO.HIGH)  
            time.sleep(queryInterval/50)
            GPIO.output(21, GPIO.LOW)
            time.sleep(queryInterval/50)
            GPIO.output(21, GPIO.HIGH)    
            time.sleep(queryInterval/50)
            GPIO.output(21, GPIO.LOW)
            time.sleep(queryInterval/50)
            GPIO.output(21, GPIO.HIGH)    
        
        # Start sensor initialization based upon quantity pin readings
        #CBM 5/15/2018 changed num to 4 (from 1),commented out lines below

       

        # Start Sensor Initialization
        # sensor = MAX31856(software_spi=software_spi)


        
        software_spi1 = {"clk": 11, "cs": 0, "do": 10, "di": 9}
        software_spi2 = {"clk": 11, "cs": 5, "do": 10, "di": 9}
        software_spi3 = {"clk": 11, "cs": 6, "do": 10, "di": 9}
        software_spi4 = {"clk": 11, "cs": 19, "do": 10, "di": 9}            
        # later on, will check for therm = 0 if it exists!

        # End sensor Initialization

        # Initialize mySql Components
        # do sql here

        # End SQL initialization
        # Begin data acquisition

        digital1Val = GPIO.input(4)
        digital2Val = GPIO.input(17)
        digital3Val = GPIO.input(27)
        digital4Val = GPIO.input(22)



        analog1Val ='NULL'
        analog2Val ='NULL'
        analog3Val ='NULL'
        analog4Val ='NULL'


        thermocouple1Val ='NULL'
        thermocouple2Val ='NULL'
        thermocouple3Val ='NULL'
        thermocouple4Val ='NULL'

        if(useSensors =='Y'):
            GPIO.output(20, GPIO.HIGH)
            if(numAnalog>0):
                # Create an ADS1015 ADC (12-bit) instance.
                adc = Adafruit_ADS1x15.ADS1015()
                # If other sensor is used, Create an ADS1015 ADC (16-bit) instance.
                # adc = Adafruit_ADS1x15.ADS1115()
                if(numAnalog == 4):
                  analog1Val = (adc.read_adc(0, gain=GAIN))*m1+b1                  
                  analog2Val = (adc.read_adc(1, gain=GAIN))*m2+b2 
                  analog3Val = (adc.read_adc(2, gain=GAIN))*m3+b3 
                  analog4Val = (adc.read_adc(3, gain=GAIN))*m4+b4 
                else:
                    if(numAnalog == 3):
                        analog1Val = (adc.read_adc(0, gain=GAIN))*m1+b1 
                        analog2Val = (adc.read_adc(1, gain=GAIN))*m2+b2 
                        analog3Val = (adc.read_adc(2, gain=GAIN))*m3+b3
                    else:
                        if (numAnalog == 2):
                            analog1Val = (adc.read_adc(0, gain=GAIN))*m1+b1 
                            analog2Val = (adc.read_adc(1, gain=GAIN))*m2+b2 
                        else:
                            if (numAnalog == 1):
                               analog1Val = (adc.read_adc(0, gain=GAIN))*m1+b1 
            else:
                GPIO.output(20, GPIO.LOW)
                analog1Val = 'NULL'
                analog2Val = 'NULL'
                analog3Val = 'NULL'
                analog4Val = 'NULL'



            if(numThermocouple>0):
                if (numThermocouple == 4):
                    therm1 = MAX31856(software_spi=software_spi1)
                    therm2 = MAX31856(software_spi=software_spi2)
                    therm3 = MAX31856(software_spi=software_spi3)
                    therm4 = MAX31856(software_spi=software_spi3)
                    thermocouple1Val = therm1.read_temp_c()
                    if (u1 == 'F'):
                        thermocouple1Val = cToF(thermocouple1Val)
                    thermocouple2Val = therm2.read_temp_c()
                    if (u2 == 'F'):
                        thermocouple2Val = cToF(thermocouple2Val)
                    thermocouple3Val = therm3.read_temp_c()
                    if (u3 == 'F'):
                        thermocouple3Val = cToF(thermocouple3Val)
                    thermocouple4Val = therm4.read_temp_c()
                    if (u4 == 'F'):
                        thermocouple4Val = cToF(thermocouple4Val)
                else:
                    if (numThermocouple == 3):
                        therm1 = MAX31856(software_spi=software_spi1)
                        therm2 = MAX31856(software_spi=software_spi2)
                        therm3 = MAX31856(software_spi=software_spi3)
                        
                        thermocouple1Val = therm1.read_temp_c()
                        if (u1 == 'F'):
                            thermocouple1Val = cToF(thermocouple1Val)
                        thermocouple2Val = therm2.read_temp_c()
                        if (u2 == 'F'):
                            thermocouple2Val = cToF(thermocouple2Val)
                        thermocouple3Val = therm3.read_temp_c()
                        if (u3 == 'F'):
                            thermocouple3Val = cToF(thermocouple3Val)
                    else:
                        if (numThermocouple == 2):
                            therm1 = MAX31856(software_spi=software_spi1)
                            therm2 = MAX31856(software_spi=software_spi2)
                    
                            thermocouple1Val = therm1.read_temp_c()
                            if (u1 == 'F'):
                                thermocouple1Val = cToF(thermocouple1Val)
                            thermocouple2Val = therm2.read_temp_c()
                            if (u2 == 'F'):
                                thermocouple2Val = cToF(thermocouple2Val)
                        else:
                            if (numThermocouple == 1):
                                therm1 = MAX31856(software_spi=software_spi1)
                    
                                thermocouple1Val = therm1.read_temp_c()
                                if (u1 == 'F'):
                                    thermocouple1Val = cToF(thermocouple1Val)
            else:
                thermocouple1Val = 'NULL'
                thermocouple2Val = 'NULL'
                thermocouple3Val = 'NULL'
                thermocouple4Val = 'NULL'
                GPIO.output(20, GPIO.LOW)
        else:
            GPIO.output(20, GPIO.LOW)# End data acquisition
        # print values for verification

        print("Digital Sensor Values: ")
        print(digital1Val)
        print(digital2Val)
        print(digital3Val)
        print(digital4Val)



        print("Analog Sensor Values: ")
        print(analog1Val)
        print(analog2Val)
        print(analog3Val)
        print(analog4Val)

        print("Thermocouple Values: ")
        print(thermocouple1Val)
        print(thermocouple2Val)
        print(thermocouple3Val)
        print(thermocouple4Val)

        sqlValuesToInsert = "NOW(),'"+ machineName + "','" + deviceName + "'"
        sqlValuesToInsert += ","
        sqlValuesToInsert +=  str(digital1Val)
        sqlValuesToInsert += ","
        sqlValuesToInsert += str(digital2Val)
        sqlValuesToInsert += ","
        sqlValuesToInsert += str(digital3Val)
        sqlValuesToInsert += ","
        sqlValuesToInsert +=  str(digital4Val)
        sqlValuesToInsert += ","
        sqlValuesToInsert += str(analog1Val)
        sqlValuesToInsert += ","
        sqlValuesToInsert +=  str(analog2Val)
        sqlValuesToInsert += ","
        sqlValuesToInsert +=  str(analog3Val)
        sqlValuesToInsert += ","
        sqlValuesToInsert += str(analog4Val)
        sqlValuesToInsert += ","
        sqlValuesToInsert +=  str(thermocouple1Val)
        sqlValuesToInsert += ","
        sqlValuesToInsert += str(thermocouple2Val)
        sqlValuesToInsert += ","
        sqlValuesToInsert +=  str(thermocouple3Val)
        sqlValuesToInsert += ","
        sqlValuesToInsert += str(thermocouple4Val)
        sqlValuesToInsert += ")"
        print(sqlValuesToInsert)
        
        insertString = "INSERT into " + machineName + ".daq "
        insertString += "(dateAndTime, machineName, deviceName, digital1, digital2, digital3, digital4,"
        insertString+= "analog1,analog2,analog3,analog4,thermocouple1,thermocouple2,thermocouple3,thermocouple4)"
      
        insertString += " VALUES (" + sqlValuesToInsert 
        print(insertString)

        if(isUtilizationONLY== 'N'):
            print("Committing now!")
            cursor.execute(insertString)
            cnx.commit()
        else:
            print("Not committing any DAQ data! This is a utilization only device.")
        cursor.close()
        cnx.close()
        
        try:
            
            if(isUtilizationDevice =='Y'):
                GPIO.output(16, GPIO.HIGH)
                print("Starting utilization commit")
                checkLastEntryString = "select machineRunning from utilizationmaster.utilization where"
                checkLastEntryString+= " machineName = '" +machineName+ "' and deviceName = '" +deviceName+"' order by datetime desc limit 1"
                print(checkLastEntryString)
                cnx2 = mysql.connector.connect(user='daq', password='dataacquisition',host='10.10.9.107')
            
                selectionCursor = cnx2.cursor()
                
                selectionCursor.execute(checkLastEntryString)
                

                try:
                    lastEntry = selectionCursor.fetchone()[0]
                except:
                    lastEntry = 'None'
                
                
                print("Last entry: "+lastEntry) 
                if (lastEntry == 'None'):                             
                    cnx2 = mysql.connector.connect(user='daq', password='dataacquisition',host='10.10.9.107')
                    cursor2 = cnx2.cursor()
                    utilizationString = "Insert into utilizationmaster.utilization(datetime,machineName,deviceName,department, machineRunning)"
                    utilizationString+= " VALUES(NOW(),'"
                    utilizationString+= machineName + "','"
                    utilizationString+= deviceName+"','"
                    utilizationString+= department + "','"          
                    utilizationString+= "0')"
                    print("Pin Value changed/ was null!")
                    print(utilizationString)
                    cursor2.execute(utilizationString)
                    cnx2.commit()
                    cursor2.close()
                    cnx2.close()
                
                utilizationVal = GPIO.input(4);
                if(isLogicalUtil):
                    logicReadPins = str(GPIO.input(4))+ str(GPIO.input(17))+ str(GPIO.input(27))+ str(GPIO.input(22))
                    print('Current pins logic = ' + logicReadPins)
                    print('As compared to defined logic of ' + logicIfIsUtil)
                    if(logicReadPins == logicIfIsUtil):
                        utilizationVal =1
                        GPIO.output(12, GPIO.HIGH)
                        print('It was a match!')
                    else:
                        utilizationVal =0
                        print('No match!')
                        GPIO.output(12, GPIO.LOW)

                    
                if(lastEntry == '0'):
                    print(utilizationVal)
                    if(utilizationVal ==1):
                        
                        cnx2 = mysql.connector.connect(user='daq', password='dataacquisition',host='10.10.9.107')
                        cursor2 = cnx2.cursor()
                        utilizationString = "Insert into utilizationmaster.utilization(datetime,machineName,deviceName,department, machineRunning)"
                        utilizationString+= " VALUES(NOW(),'"
                        utilizationString+= machineName+ "','"
                        utilizationString+= deviceName+"','"
                        utilizationString+= department + "','"          
                        utilizationString+= "1')"
                        print("Pin Value changed to 1!")
                        print(utilizationString)
                        cursor2.execute(utilizationString)
                        cnx2.commit()
                        cursor2.close()
                        cnx2.close()
                    else:
                        print("No 0=>1 change.")

                if(lastEntry =='1'):
                    if(utilizationVal ==0):
                        
                        cnx2 = mysql.connector.connect(user='daq', password='dataacquisition',host='10.10.9.107')
                        cursor2 = cnx2.cursor()
                        utilizationString = "Insert into utilizationmaster.utilization(datetime,machineName,deviceName,department, machineRunning)"
                        utilizationString+= " VALUES(NOW(),'"
                        utilizationString+= machineName+ "','"
                        utilizationString+= deviceName+"','"
                        utilizationString+= department + "','"          
                        utilizationString+= "0')"
                        print("Pin Value changed to 0!")
                        cursor2.execute(utilizationString)
                        cnx2.commit()
                        cursor2.close()
                        cnx2.close()
                        
                    else:
                        print("No 1=>0 change.")
            else:
                 GPIO.output(16, GPIO.LOW)

        except:
            print("Error in utilization commit")
            for errloop in range(50):
                GPIO.output(21, GPIO.HIGH)
                GPIO.output(20, GPIO.LOW)
                GPIO.output(16, GPIO.LOW)
                GPIO.output(12, GPIO.HIGH)
                time.sleep(.1)
                GPIO.output(21, GPIO.LOW)
                GPIO.output(20, GPIO.HIGH)
                GPIO.output(16, GPIO.HIGH)
                GPIO.output(12, GPIO.LOW)
                time.sleep(.1)
    except:
        print("Error! Something went wrong in the main loop")
        for errloop in range(5):
            GPIO.output(21, GPIO.HIGH)
            GPIO.output(20, GPIO.HIGH)
            GPIO.output(16, GPIO.HIGH)
            GPIO.output(12, GPIO.HIGH)
            time.sleep(.5)
            GPIO.output(21, GPIO.LOW)
            GPIO.output(20, GPIO.LOW)
            GPIO.output(16, GPIO.LOW)
            GPIO.output(12, GPIO.LOW)
            time.sleep(.5)
            try:
                testIP = "8.8.8.8"
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect((testIP, 0))
                ipaddr = s.getsockname()[0]
                print(ipaddr)
                one = 21
                two = 20
                three = 16
                four = 12
                ipaddr = str(ipaddr)
                for l in range(2):
                    print()
                    for c in ipaddr:
                        print(c)
                        if(c=='0'):
                            GPIO.output(one, GPIO.HIGH)
                            GPIO.output(two, GPIO.HIGH)
                            GPIO.output(three, GPIO.HIGH)
                            GPIO.output(four, GPIO.HIGH)
                            time.sleep(1)
                        if(c=='1'):
                            GPIO.output(one, GPIO.HIGH)
                            GPIO.output(two, GPIO.LOW)
                            GPIO.output(three, GPIO.LOW)
                            GPIO.output(four, GPIO.LOW)
                            time.sleep(1)
                        if(c=='2'):
                            GPIO.output(one, GPIO.LOW)
                            GPIO.output(two, GPIO.HIGH)
                            GPIO.output(three, GPIO.LOW)
                            GPIO.output(four, GPIO.LOW)
                            time.sleep(1)
                        if(c=='3'):
                            GPIO.output(one, GPIO.LOW)
                            GPIO.output(two, GPIO.LOW)
                            GPIO.output(three, GPIO.HIGH)
                            GPIO.output(four, GPIO.LOW)
                            time.sleep(1)
                        if(c=='4'):
                            GPIO.output(one, GPIO.LOW)
                            GPIO.output(two, GPIO.LOW)
                            GPIO.output(three, GPIO.LOW)
                            GPIO.output(four, GPIO.HIGH)
                            time.sleep(1)
                        if(c=='5'):
                            GPIO.output(one, GPIO.HIGH)
                            GPIO.output(two, GPIO.LOW)
                            GPIO.output(three, GPIO.LOW)
                            GPIO.output(four, GPIO.HIGH)
                            time.sleep(1)
                        if(c=='6'):
                            GPIO.output(one, GPIO.LOW)
                            GPIO.output(two, GPIO.HIGH)
                            GPIO.output(three, GPIO.LOW)
                            GPIO.output(four, GPIO.HIGH)
                            time.sleep(1)
                        if(c=='7'):
                            GPIO.output(one, GPIO.LOW)
                            GPIO.output(two, GPIO.LOW)
                            GPIO.output(three, GPIO.HIGH)
                            GPIO.output(four, GPIO.HIGH)
                            time.sleep(1)
                        if(c=='8'):
                            GPIO.output(one, GPIO.HIGH)
                            GPIO.output(two, GPIO.LOW)
                            GPIO.output(three, GPIO.HIGH)
                            GPIO.output(four, GPIO.HIGH)
                            time.sleep(1)
                        if(c=='9'):
                            GPIO.output(one, GPIO.LOW)
                            GPIO.output(two, GPIO.HIGH)
                            GPIO.output(three, GPIO.HIGH)
                            GPIO.output(four, GPIO.HIGH)
                            time.sleep(1)
                        if(c=='.'):
                            GPIO.output(one, GPIO.HIGH)
                            GPIO.output(two, GPIO.HIGH)
                            GPIO.output(three, GPIO.HIGH)
                            GPIO.output(four, GPIO.HIGH)
                            time.sleep(.25)
                            GPIO.output(one, GPIO.LOW)
                            GPIO.output(two, GPIO.LOW)
                            GPIO.output(three, GPIO.LOW)
                            GPIO.output(four, GPIO.LOW)
                            time.sleep(.25)
                            GPIO.output(one, GPIO.HIGH)
                            GPIO.output(two, GPIO.HIGH)
                            GPIO.output(three, GPIO.HIGH)
                            GPIO.output(four, GPIO.HIGH)
                            time.sleep(.25)
                            GPIO.output(one, GPIO.LOW)
                            GPIO.output(two, GPIO.LOW)
                            GPIO.output(three, GPIO.LOW)
                            GPIO.output(four, GPIO.LOW)
                            time.sleep(.25)
                    GPIO.output(21, GPIO.LOW)
                    GPIO.output(20, GPIO.LOW)
                    GPIO.output(16, GPIO.LOW)
                    GPIO.output(12, GPIO.LOW)
            except:
                print("Error")
            

        

    
                
                
            
        


        
        

        
        
        #host = socket.gethostname()
        #print(host)
print(sqlValuesToInsert)
