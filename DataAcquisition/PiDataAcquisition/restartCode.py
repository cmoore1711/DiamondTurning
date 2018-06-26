import os
import time
import psutil



isPiDaqCodeRunning = False
isTimeKeeperRunning = False



for pid in psutil.pids():
    p = psutil.Process(pid)
    if(p.name() == "python3" and len(p.cmdline()) >1 and "piDaqCode.py" in p.cmdline()[1]):
        isPiDaqCodeRunning = True
    if(p.name() == "python3" and len(p.cmdline()) >1 and "pythonTimeSync.py" in p.cmdline()[1]):
        isTimeKeeperRunning = True
        #print(p.cmdline()[1])
        #
print(isPiDaqCodeRunning)
print(isTimeKeeperRunning)


os.system("cd /home/pi/Desktop/PiDataAcquisition && sudo git pull")

if(not isPiDaqCodeRunning):

    os.system("cd && python3 Desktop/PiDataAcquisition/PiDataAcquisition/piDaqCode.py")
if(not isTimeKeeperRunning):
    os.system("cd && python3 Desktop/PiDataAcquisition/PiDataAcquisition/pythonTimeSync.py")




##os.system(changeTimeString)
##ps -aef | grep python
