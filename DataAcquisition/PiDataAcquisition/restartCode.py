import os
import time
import psutil




isTimeKeeperRunning = False



for pid in psutil.pids():
    p = psutil.Process(pid)
    if(p.name() == "python3" and len(p.cmdline()) >1 and "pythonTimeSync.py" in p.cmdline()[1]):
        isTimeKeeperRunning = True
        #print(p.cmdline()[1])
        #

print(isTimeKeeperRunning)


os.system("cd /home/pi/Desktop/DiamondTurning && sudo git pull")

if(not isTimeKeeperRunning):
    os.system("cd && python3 Desktop/PiDataAcquisition/PiDataAcquisition/pythonTimeSync.py")




##os.system(changeTimeString)
##ps -aef | grep python
