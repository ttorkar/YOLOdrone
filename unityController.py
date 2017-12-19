#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import json

host = 'localhost' 
port = 50000
backlog = 5 
size = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(backlog) 

while 1:
    client, address = s.accept() 
    print ("Client connected.")
    while 1:
        data = client.recv(size)
        if data:
            parsed_json = json.loads(data)
            print ("Unity Sent: " + str(parsed_json))
            client.send(parsed_json)
            