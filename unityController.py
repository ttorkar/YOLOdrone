#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import json
import threading
import struct

host = 'localhost' 
port = 50000
backlog = 5 
size = 1024 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.bind((host,port)) 
sock.listen(backlog) 

def server(client, address):
    FILEINFO_SIZE = struct.calcsize('128sI')
    while True:
        try:
            fhead = newsock.recv(FILEINFO_SIZE)
            filename, filesize = struct.unpack('128sI', fhead)
            ''' To unpack the received data ， According to the packing rules 128sI'''
            print("The address is: ", address)
            print(filename, len(filename), type(filename))
            print(filesize)
        except Exception as e:
            print('Exception: ', e)


while True:
    client, address = sock.accept() 
    print ("Client {} connected on Address {}.".format(client, address))
    while True:
        tmpThread = threading.Thread(target=server, args=(client, address)) #  If the file is received ， Create thread 
        tmpThread.start() #  Execution thread 
    #        data = client.recv(size)
    #        if data:
    #            parsed_json = json.loads(data)
    #            print ("Unity Sent: " + str(parsed_json))
    #            client.send(parsed_json)
#            