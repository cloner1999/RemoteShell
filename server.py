################# Coded By $0lD3R



#!/usr/bin/python

# Remote Windows Prompt / Shell
# SERVER


import os
import sys
import socket

Host = '127.0.0.1'
Port = 8888

error = "Error : Socket\n"
adrs = (Host, Port)
Buff = 64790

SockServ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    SockServ.bind(adrs)
    SockServ.listen(5)
    print "\n\a[*]Server Listenning on port ", Port, " [Waiting...].\n"
except socket.error:
    print error
    raw_input("Press Enter to Continue..")

connexion, adresse = SockServ.accept()

print "\n\a[*]New Connection ~ IP: %s, Port: %s\n" % (adresse[0], adresse[1])


while True:

    connexion.send("cmd")
    
    cmd = raw_input("root@shell# ")

    if cmd == "/disconnect":

        connexion.send("close~cmd")
        data = connexion.recv(Buff)
        print ""
        print data
        break

    elif cmd == "":

        print "\nCommand Not Found...\n"

    else:
		try:
			connexion.send(cmd)
			data = connexion.recv(Buff)
			print ""
			print data, "\n"
		except:
			pass
