======================
IEEE488-Quancom-python
======================

This is a wrapper class for communicating with the
Quancom IEEE488 (GPIB) PCI card (PCIGPIB-1) through 
the Quancom Qlib software library. Only minimal read 
and write functionality is implemented.

For more information see 
http://www.quancom.de/
http://www.quancom.com/manual/manual_english_qlib/index.html?qlib_kurzeinf.htm

Usage:
1. Import module: 

> from ieeeinterface import IEEEInterface

2. Make an instance of the interface: 

> myIEEE=IEEEInterface()

3. Open connection to card: 

> cardhandle=myIEEE.openCard()

4. Check if opened successfully - if cardhandle is 0 then an error occurred - alert user and exit().   
Note: opening card and checking needs only be done once per program

5. To read from device (e.g if device id is 5):

> device=5
> response=myIEEE.readDevice(device)

"response" is a string. 
If response is empty then an error occurred and you should try a re-read. 
If response is not empty, then extract the number from the string and store/save/plot as appropriate.
Note: readDevice() tries 5 times for a successful read before returning.



Installation & Upgrade
======================

Download zip and cd to IEEE488-Quancom-python folder.

To install: pip install .

To upgrade: pip install --upgrade .

To remove: pip uninstall ieeeinterface
