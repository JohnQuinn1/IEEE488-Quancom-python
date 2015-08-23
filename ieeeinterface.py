# -*- coding: utf-8 -*-


from ctypes import windll
from ctypes import c_char_p
import types


class IEEEInterface:

    # Loads up the dll from the c:\windows\system32 folder
    # Functions are accessed as attributes of dll objects:
    def __init__(self):
        print("Initialised interface")
        self.myDLL = windll.qlib32
        self.cardOpen = False
    
    # 54 is the cardid specific to the card I'm using as far as I can remember
    def openCard(self):
        self.cardhandle = self.myDLL.QAPIExtOpenCard(54, 0)
        self.cardOpen = True if self.cardhandle != 0 else False
        return self.cardhandle

    def closeCard(self):
        self.myDLL.QAPIExtCloseCard(self.cardhandle)
        self.cardOpen = False

    # Tries at most 5 times to read device
    def readDevice(self, device):
        buffer = c_char_p(b"")
        readSuccessful = i = 0
        while(!readSuccessful and i < 5):
            readSuccessful = self.myDLL.QAPIExtReadString(self.cardhandle, device, buffer, 1000, 0)
            i += 1
        return buffer.value.decode('utf-8')

    def writeDevice(self, device, string):
        buffer = c_char_p(bytes(string, 'utf-8'))
        # strncpy(tmp, str.c_str(), 1000);
        return bool(self.myDLL.QAPIExtWriteString(self.cardhandle, device, buffer, len(string), 0))

    def __getattr__(self, name):
            def myfunc(self, *args):
                return eval("self.myDLL.QAPI"+name+"(*args)")
            meth = types.MethodType(myfunc, self)
            return meth
