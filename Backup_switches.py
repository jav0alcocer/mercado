# -*- coding: cp1252 -*-
import getpass
import sys
import telnetlib
import time
import os
import errno
import os.path

##getting system date 
day=time.strftime('%d')
month=time.strftime('%m')
year=time.strftime('%Y')
hour=time.strftime('%H')
minute=time.strftime('%M')
second=time.strftime('%M')
today=day+month+year+'_'+hour+minute+second

ipfile=open("iplist.txt")

for line in ipfile:
    try:
        credenciales = line.split('\n')[0].split(',')
        HOST = credenciales[0]
        user = credenciales[1]
        password = credenciales[2]
        hostname = credenciales[3]
        pathdir = "C:\\Users\\INTELICO\\mercado\\"
        tn = telnetlib.Telnet(HOST,23,5)
        
        if not (os.path.exists('C:\\Users\\INTELICO\\mercado\\')):
            os.mkdir(pathdir + HOST)
        file = open(pathdir + HOST+"\\" + HOST +'_'+today+".txt","w+")
        log = ""
        tn.read_until("User: ")
        tn.write(user + "\n")
        tn.read_until("Password: ")
        tn.write(password + "\n")
        tn.read_until(credenciales[3] + " *")
        tn.write("config\n")
        tn.read_until(credenciales[3] + " Config>")
        tn.write("show all-config\n")
        log = log + tn.read_until(credenciales[3]+ " Config>")
        tn.write("end\n")
        tn.read_until(credenciales[3] + " *")
        tn.write("logout\n")
        tn.read_until("Do you wish to end connection (Yes/No)? ")
        tn.write("Yes\n")
        file.write(log)
        file.close()
    except OSError as e:
        if e.errno !=errno.EEXIST:
            raise
    except:
        print("NO SE ENCUENTRA CONECTADO EL EQUIPO " + (HOST))
