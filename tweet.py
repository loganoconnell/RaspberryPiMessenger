#!/usr/bin/env python
import sys, os
from twython import Twython

def getRecentConnections():
    theFile = open('/var/log/openvpn.log','r')
    FILE = theFile.readlines()
    theFile.close()
    MBPList = []
    iP6List = []
    iP5sList = []
    for line in FILE:
        if ('Initiated' in line):
            if ('Logans-MBP' in line):
                MBPList.append(line)
	    elif ('Logans-iPhone6' in line):
		iP6List.append(line)
	    else:
		iP5sList.append(line)
    
    finalList = []
    finalList.append(MBPList[-1:])
    finalList.append(iP6List[-1:])
    finalList.append(iP5sList[-1:])

    stringList = []

    for item in finalList:
        str = ''.join(item)
	stringList.append(str)

    return stringList

def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            return(line.split()[1:4])
                                
def getCPUuse():
    return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip(\
)))

def getDiskSpace():
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i +1
        line = p.readline()
        if i==2:
            return(line.split()[1:5])

recent_connections = getRecentConnections()

CPU_temp = getCPUtemperature()
CPU_usage = getCPUuse()

RAM_stats = getRAMinfo()
RAM_total = round(int(RAM_stats[0]) / 1000,1)
RAM_used = round(int(RAM_stats[1]) / 1000,1)
RAM_free = round(int(RAM_stats[2]) / 1000,1)

DISK_stats = getDiskSpace()
DISK_total = DISK_stats[0]
DISK_free = DISK_stats[1]
DISK_perc = DISK_stats[3]

tweetStr = 'All systems are up and running.' + '\n\nRecent Connections:\n' + '- ' + recent_connections[0] + '- ' + recent_connections[1] + '- ' + recent_connections[2] + '\n\nSystem Statistics:\n- CPU Temperature: ' + CPU_temp + 'F' + ' \n- CPU Usage: ' + CPU_usage + '%' + '\n- Total RAM: ' + str(RAM_total) + 'M' + '\n- Used RAM: ' + str(RAM_used) + 'M' + '\n- Free RAM: ' + str(RAM_free) + 'M' + '\n- Total Disk Space: ' + str(DISK_total) + '\n- Free Disk Space: ' + str(DISK_free) + '\n- Percentage of Disk Spaced Used: ' + str(DISK_perc)

apiKey = ''
apiSecret = ''
accessToken = ''
accessTokenSecret = ''

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

api.send_direct_message(screen_name='',text=tweetStr)

print 'Sent Message: ' + tweetStr
