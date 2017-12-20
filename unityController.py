#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
from PIL import Image
import io
import threading
from darkflow.net.build import TFNet

host = 'localhost' 
port = 50000
backlog = 20 
size = 1024
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(backlog) 

def display(image, count):
    image.show()
    image.save('images/image_{}.jpg'.format(count), "JPEG")
    image.close()
    

def recieveMsg(client, address):
    count = 0
    while True:  
        
        length = int(client.recv(size).decode())
        print(length)
        data = b''
        while len(data) < length:
            # doing it in batches is generally better than trying
            # to do it all in one go, so I believe.
            to_read = length - len(data)
            chunk_size = 1024 if to_read > 1024 else to_read
            chunk = client.recv(chunk_size)
            data += chunk
        image = Image.open(io.BytesIO(data))
        tmpThread = threading.Thread(target=display, args=(image, count)) #  If the file is received ， Create thread 
        tmpThread.start() #  Execution thread 
        count += 1




while True:
    print('Waiting for Connection')
    client, address = s.accept() 
    print ("Client connected on {}.".format(address))
    recieveMsg(client, address)
#    tmpThread = threading.Thread(target=recieveMsg, args=(client, address)) #  If the file is received ， Create thread 
#    tmpThread.start() #  Execution thread 

               
