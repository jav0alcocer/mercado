#!/usr/bin/python
import getpass
import sys
import telnetlib
import time

##getting system date 
day=time.strftime('%d')
month=time.strftime('%m')
year=time.strftime('%Y')
today=day+"-"+month+"-"+year

HOST = "189.146.252.20"
user = "intelico"
password = "intelico"
file = open(HOST + '_' +today+".txt","w+")
log = ""
tn = telnetlib.Telnet(HOST)
tn.read_until("User: ")
tn.write(user + "\n")
tn.read_until("Password: ")
tn.write(password + "\n")
tn.read_until("INTELICO *")
tn.write("config\n")
tn.read_until("INTELICO Config>")
tn.write("show all-config\n")
log = log + tn.read_until("INTELICO Config>")
tn.write("end\n")
tn.read_until("INTELICO *")
tn.write("logout\n")
tn.read_until("Do you wish to end connection (Yes/No)? ")
tn.write("Yes\n")
file.write(log)
file.close()