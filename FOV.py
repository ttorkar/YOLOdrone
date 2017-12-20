#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math as m


x1 = 150
y1 = 100
x2 = 200
y2 = 200

imageWidth = 416
imageHeight = 416

FOVxRadians = m.radians(60)

def changeCoordinates(x,y, imageWidth, imageHeight):
    return x - imageWidth / 2, y - imageHeight / 2

def getCentre(x1,y1,x2,y2):
    xWidth = (x2 - x1) 
    yHeight = (y2 - y1) 
    X1 = x1 + xWidth / 2
    Y1 = y1 + yHeight / 2
    return X1, Y1

def getPhi(X, Y):
    phi = m.atan2(Y,X)
    if phi < 0: phi = 2*m.pi+phi
    return phi

def getTheta(X, Y, FOVxRadians, imageWidth):
    r = m.sqrt(X**2 + Y**2)
    theta = m.pi - ((FOVxRadians / imageWidth) * r )
    return theta
    

X1, Y1 = getCentre(x1,y1,x2,y2)
X, Y = changeCoordinates(X1, Y1, imageWidth, imageHeight)


phi = getPhi(X,Y)
theta = getTheta(X,Y, FOVxRadians, imageWidth)
print('Phi: {}, Theta: {}'.format(phi, theta))