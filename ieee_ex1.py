# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 11:47:12 2014

@author: Marco Forte

@description: Attempts to read value from device(Pico Ammeter) and 
prints value as float
"""

from ieeeinterface import IEEEInterface
import sys
myCard = IEEEInterface()

cardhandle = myCard.openCard()

if(cardhandle ==0):
    print("Error - could not open card, exiting...")
    sys.exit()
else:
    print("Card opened successfully!, card handle is: " + str(cardhandle))

device = 5
response = myCard.readDevice(device)

if(response == ""):
    print("Error - could not read from device: " + str(device) + ", exiting...")
    sys.exit()
else:
    print("Recieved response, " + response)
    
floatValue = float(response[4:])

print("Converted to double")
print(floatValue)

myCard.closeCard()
