#!/usr/bin/python3

#
# Misc methods to retrieve system information.
#

import os
import time
import socket
import psutil

def argonsysinfo_listcpuusage(sleepsec = 1):
    outputlist = []
    curusage_a = argonsysinfo_getcpuusagesnapshot()
    time.sleep(sleepsec)
    curusage_b = argonsysinfo_getcpuusagesnapshot()

    for cpuname in curusage_a:
        if cpuname == "cpu":
            continue
        if curusage_a[cpuname]["total"] == curusage_b[cpuname]["total"]:
            outputlist.append({"title": cpuname, "value": "0%"})
        else:
            total = curusage_b[cpuname]["total"]-curusage_a[cpuname]["total"]
            idle = curusage_b[cpuname]["idle"]-curusage_a[cpuname]["idle"]
            outputlist.append({"title": cpuname, "value": int(100*(total-idle)/(total))})
    return outputlist

def argonsysinfo_getcpuusagesnapshot():
    cpupercent = {}
    errorflag = False
    try:
        cpuctr = 0
        # user, nice, system, idle, iowait, irc, softirq, steal, guest, guest nice
        tempfp = open("/proc/stat", "r")
        alllines = tempfp.readlines()
        for temp in alllines:
            temp = temp.replace('\t', ' ')
            temp = temp.strip()
            while temp.find("  ") >= 0:
                temp = temp.replace("  ", " ")
            if len(temp) < 3:
                cpuctr = cpuctr +1
                continue

            checkname = temp[0:3]
            if checkname == "cpu":
                infolist = temp.split(" ")
                idle = 0
                total = 0
                colctr = 1
                while colctr < len(infolist):
                    curval = int(infolist[colctr])
                    if colctr == 4 or colctr == 5:
                        idle = idle + curval
                    total = total + curval
                    colctr = colctr + 1
                if total > 0:
                    cpupercent[infolist[0]] = {"total": total, "idle": idle}
            cpuctr = cpuctr +1

        tempfp.close()
    except IOError:
        errorflag = True
    return cpupercent


def argonsysinfo_liststoragetotal():
    outputlist = []
    ramtotal = 0
    errorflag = False

    try:
        hddctr = 0
        tempfp = open("/proc/partitions", "r")
        alllines = tempfp.readlines()

        for temp in alllines:
            temp = temp.replace('\t', ' ')
            temp = temp.strip()
            while temp.find("  ") >= 0:
                temp = temp.replace("  ", " ")
            infolist = temp.split(" ")
            if len(infolist) >= 4:
                # Check if header
                if infolist[3] != "name":
                    parttype = infolist[3][0:3]
                    if parttype == "ram":
                        ramtotal = ramtotal + int(infolist[2])
                    elif parttype[0:2] == "sd" or parttype[0:2] == "hd":
                        lastchar = infolist[3][-1]
                        if lastchar.isdigit() == False:
                            outputlist.append({"title": infolist[3], "value": argonsysinfo_kbstr(int(infolist[2]))})
                    else:
                        # SD Cards
                        lastchar = infolist[3][-2]
                        if lastchar[0] != "p":
                            outputlist.append({"title": infolist[3], "value": argonsysinfo_kbstr(int(infolist[2]))})

        tempfp.close()
        #outputlist.append({"title": "ram", "value": argonsysinfo_kbstr(ramtotal)})
    except IOError:
        errorflag = True
    return outputlist

def argonsysinfo_getram():
    totalram = 0
    totalfree = 0
    tempfp = open("/proc/meminfo", "r")
    alllines = tempfp.readlines()

    for temp in alllines:
        temp = temp.replace('\t', ' ')
        temp = temp.strip()
        while temp.find("  ") >= 0:
            temp = temp.replace("  ", " ")
        infolist = temp.split(" ")
        if len(infolist) >= 2:
            if infolist[0] == "MemTotal:":
                totalram = int(infolist[1])
            elif infolist[0] == "MemFree:":
                totalfree = totalfree + int(infolist[1])
            elif infolist[0] == "Buffers:":
                totalfree = totalfree + int(infolist[1])
            elif infolist[0] == "Cached:":
                totalfree = totalfree + int(infolist[1])
    if totalram == 0:
        return "0%"
    return [str(int(100*totalfree/totalram))+"%", str((totalram+512*1024)>>20)+"GB"]


def argonsysinfo_gettemp():
    try:
        tempfp = open("/sys/class/thermal/thermal_zone0/temp", "r")
        temp = tempfp.readline()
        tempfp.close()
        return float(int(temp)/1000)
    except IOError:
        return 0
    cval = val/1000
    fval = 32+9*val/5000

def argonsysinfo_getip():
    ipaddr = ""
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try: 
        # Connect to nonexistent device
        st.connect(('254.255.255.255', 1))
        ipaddr = st.getsockname()[0]
    except Exception:
        ipaddr = 'N/A'
    finally:
        st.close()
    return ipaddr

def get_ip_addresses( family ):
    for interface, snics in psutil.net_if_addrs().items():
        if interface != "lo":
            for snic in snics:
                if snic.family == family:
                    yield( interface, snic.address )

def argonsysinfo_getipList():
    iplist = []
    iplist = list(get_ip_addresses( socket.AF_INET ))

    return iplist

def argonsysinfo_getrootdev():
    tmp = os.popen('mount').read()
    alllines = tmp.split("\n")

    for temp in alllines:
        temp = temp.replace('\t', ' ')
        temp = temp.strip()
        while temp.find("  ") >= 0:
            temp = temp.replace("  ", " ")
        infolist = temp.split(" ")
        if len(infolist) >= 3:

            if infolist[2] == "/":
                return infolist[0]
    return ""

def argonsysinfo_listhddusage():
    outputobj = {}
    raidlist = argonsysinfo_listraid()
    raiddevlist = []
    raidctr = 0
    while raidctr < len(raidlist['raidlist']):
        raiddevlist.append(raidlist['raidlist'][raidctr]['title'])
        raidctr = raidctr + 1

    rootdev = argonsysinfo_getrootdev()

    tmp = os.popen('df').read()
    alllines = tmp.split("\n")

    for temp in alllines:
        temp = temp.replace('\t', ' ')
        temp = temp.strip()
        while temp.find("  ") >= 0:
            temp = temp.replace("  ", " ")
        infolist = temp.split(" ")
        if len(infolist) >= 6:
            if infolist[1] == "Size":
                continue
            if len(infolist[0]) < 5:
                continue
            elif infolist[0][0:5] != "/dev/":
                continue
            curdev = infolist[0]
            if curdev == "/dev/root" and rootdev != "":
                curdev = rootdev
            tmpidx = curdev.rfind("/")
            if tmpidx >= 0:
                curdev = curdev[tmpidx+1:]
            #
            # Throw out all devices being used by raid
            #
            if curdev in raidlist['hddlist']:
                continue
            elif curdev not in raiddevlist:
              if curdev[0:2] == "sd" or curdev[0:2] == "hd":
                  curdev = curdev[0:-1]
              else:
                  curdev = curdev[0:-2]
            if curdev in outputobj:
                outputobj[curdev] = {"used":outputobj[curdev]['used']+int(infolist[2]), "total":outputobj[curdev]['total']+int(infolist[1])}
            else:
                outputobj[curdev] = {"used":int(infolist[2]), "total":int(infolist[1])}

    return outputobj

def argonsysinfo_kbstr(kbval, wholenumbers = True):
    remainder = 0
    suffixidx = 0
    suffixlist = ["KB", "MB", "GB", "TB"]
    while kbval > 1023 and suffixidx < len(suffixlist):
        remainder = kbval & 1023
        kbval  = kbval >> 10
        suffixidx = suffixidx + 1

    #return str(kbval)+"."+str(remainder) + suffixlist[suffixidx]
    remainderstr = ""
    if kbval < 100 and wholenumbers == False:
        remainder = int((remainder+50)/100)
        if remainder > 0:
            remainderstr = "."+str(remainder)
    elif remainder >= 500:
        kbval = kbval + 1
    return str(kbval)+remainderstr + suffixlist[suffixidx]

def argonsysinfo_listraid():
    hddlist = []
    outputlist = []
    # cat /proc/mdstat
    # multiple mdxx from mdstat
    # mdadm -D /dev/md1

    ramtotal = 0
    errorflag = False
    try:
        hddctr = 0
        tempfp = open("/proc/mdstat", "r")
        alllines = tempfp.readlines()
        for temp in alllines:
            temp = temp.replace('\t', ' ')
            temp = temp.strip()
            while temp.find("  ") >= 0:
                temp = temp.replace("  ", " ")
            infolist = temp.split(" ")
            if len(infolist) >= 4:

                # Check if raid info
                if infolist[0] != "Personalities" and infolist[1] == ":":
                    devname = infolist[0]
                    raidtype = infolist[3]
                    raidstatus = infolist[2]
                    hddctr = 4
                    while hddctr < len(infolist):
                        tmpdevname = infolist[hddctr]
                        tmpidx = tmpdevname.find("[")
                        if tmpidx >= 0:
                            tmpdevname = tmpdevname[0:tmpidx]
                        hddlist.append(tmpdevname)
                        hddctr = hddctr + 1
                    devdetail = argonsysinfo_getraiddetail(devname)
                    outputlist.append({"title": devname, "value": raidtype, "info": devdetail})

        tempfp.close()
    except IOError:
        # No raid
        errorflag = True

    return {"raidlist": outputlist, "hddlist": hddlist}


def argonsysinfo_getraiddetail(devname):
    state = ""
    raidtype = ""
    size = 0
    used = 0
    total = 0
    working = 0
    active = 0
    failed = 0
    spare = 0
    resync = ""
    tmp = os.popen('mdadm -D /dev/'+devname).read()
    alllines = tmp.split("\n")

    for temp in alllines:
        temp = temp.replace('\t', ' ')
        temp = temp.strip()
        while temp.find("  ") >= 0:
            temp = temp.replace("  ", " ")
        infolist = temp.split(" : ")
        if len(infolist) == 2:
            if infolist[0].lower() == "raid level":
                raidtype = infolist[1]
            elif infolist[0].lower() == "array size":
                tmpidx = infolist[1].find(" ")
                if tmpidx > 0:
                    size = (infolist[1][0:tmpidx])
            elif infolist[0].lower() == "used dev size":
                tmpidx = infolist[1].find(" ")
                if tmpidx > 0:
                    used = (infolist[1][0:tmpidx])
            elif infolist[0].lower() == "state":
                state = infolist[1]
            elif infolist[0].lower() == "total devices":
                total = infolist[1]
            elif infolist[0].lower() == "active devices":
                active = infolist[1]
            elif infolist[0].lower() == "working devices":
                working = infolist[1]
            elif infolist[0].lower() == "failed devices":
                failed = infolist[1]
            elif infolist[0].lower() == "spare devices":
                spare = infolist[1]
            elif infolist[0].lower() == "rebuild status":
                resync = infolist[1]
    return {"state": state, "raidtype": raidtype, "size": int(size), "used": int(used), "devices": int(total), "active": int(active), "working": int(working), "failed": int(failed), "spare": int(spare), "resync": resync}

