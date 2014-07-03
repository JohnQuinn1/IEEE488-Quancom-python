# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 14:33:10 2014

@author: Marco Forte
"""

from ctypes import *

cardid = 54


myDLL = windll.qlib32
cardhandle = myDLL.QAPIExtOpenCard(54,0)

buffer = c_char_p(b"")
isStringReturned = i = 0
while(isStringReturned == 0 and  i < 5):
    isStringReturned = myDLL.QAPIExtReadString(cardhandle,1,buffer,1000,0)
    i = i+1
print("Read from card")
print(buffer.value.decode('utf-8'))

myDLL.QAPIExtCloseCard(cardhandle)