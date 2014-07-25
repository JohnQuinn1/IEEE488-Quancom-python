# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 14:33:10 2014

@author: Marco Forte
@desciption: This doesn't use the ieeeinterface I made but is a test I
 made while making the interface. I reads a string from the card and print it.
"""

from ctypes import windll
from ctypes import c_char_p

cardid = 54


myDLL = windll.qlib32
cardhandle = myDLL.QAPIExtOpenCard(54, 0)

buffer = c_char_p(b"")
isStringReturned = i = 0
while(isStringReturned == 0 and i < 5):
    isStringReturned = myDLL.QAPIExtReadString(cardhandle, 1, buffer, 1000, 0)
    i = i+1
print("Read from card")
print(buffer.value.decode('utf-8'))

myDLL.QAPIExtCloseCard(cardhandle)
