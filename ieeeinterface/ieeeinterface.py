# -*- coding: utf-8 -*-


from ctypes import windll
from ctypes import c_char_p
import types


class IEEEInterface:

    # Loads up the dll from the c:\windows\system32 folder
    # Functions are accessed as attributes of dll objects:
    def __init__(self):
        print("Initialised IEEE488 interface")
        self.myDLL = windll.qlib32
        self.cardOpen = False

    def __del__(self):
        if self.cardOpen:
            closeCard()

    # 54 is the cardid specific to the card I'm using as far as I can remember
    def openCard(self):
        """ Establish connection with Quancom GBIP card"""
        self.cardhandle = self.myDLL.QAPIExtOpenCard(54, 0)
        self.cardOpen = True if self.cardhandle != 0 else False
        return self.cardhandle

    def closeCard(self):
        self.myDLL.QAPIExtCloseCard(self.cardhandle)
        self.cardOpen = False

    def readDevice(self, device):
        """ Read from device returning a string,
         which is empty of the read failed."""
        buffer=create_string_buffer(1024)
        readSuccessful = self.myDLL.QAPIExtReadString(self.cardhandle,
                                                      device,
                                                      buffer,
                                                      1024, 0)
        return buffer.value.decode('utf-8')

    def writeDevice(self, device, string):
        """ Write a string to the device. """
        buffer = c_char_p(bytes(string, 'utf-8'))
        return bool(self.myDLL.QAPIExtWriteString(self.cardhandle,
                                                  device,
                                                  buffer,
                                                  len(string), 0))

    def __getattr__(self, name):
            def myfunc(self, *args):
                return eval("self.myDLL.QAPI"+name+"(*args)")
            meth = types.MethodType(myfunc, self)
            return meth
