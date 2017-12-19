#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import json
import threading
import struct

host = 'localhost' 
port = 50000
backlog = 20 
size = 1000000 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(backlog) 

def function(client, address):
    while True:
        length = client.recv(1024).decode()
        data = b''
        while len(data) < length:
            # doing it in batches is generally better than trying
            # to do it all in one go, so I believe.
            to_read = length - len(data)
            data += client.recv(4096 if to_read > 4096 else to_read)
        print(data)
        
#    data = client.recv(size)
#    if data:
##            print(data.decode())
#        try:
#            json_data = json.loads(data.decode())
#            print(json_data)
#        except:
#            print('\n\nUnable to read: \n\n', data)

    

while True:
    print('Waiting for Connection')
    client, address = s.accept() 
    print ("Client {} connected on {}.".format(client, address))
    tmpThread = threading.Thread(target=function, args=(client, address)) #  If the file is received ， Create thread 
    tmpThread.start() #  Execution thread 

               
