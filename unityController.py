#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import json
import io

host = 'localhost' 
port = 50000
backlog = 20 
size = 1000000 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(backlog) 

while True:
    print('Waiting for Connection')
    client, address = s.accept() 
    print ("Client connected.")
    while True:
        data = client.recv(size)
        if data:
#            print(data.decode())
            try:
                json_data = json.loads(data.decode())
                print(json_data)
            except:
                print('\n\nUnable to read: \n\n', data)
    
               
