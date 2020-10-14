import os
import iwlist
from termcolor import colored
# display some additional information from a wireless network interface with iwlist

# iwlist was added from  https://github.com/iancoleman/python-iwlist


'''

This is a simple protection tool against evil twin attack.

the idea is to preform a scan over an interface network trrafic.
by logic this tool checks if traffic was recived from more than one mac address, under the same SSID (Name)
if so, it alerts the user. 


    Each SSID can use specific authentication and encryption settings,
     enabling you to configure differing levels of security for different resources.
    By default, the authentication/encryption is set to none.

'''


def detect_malicious_activity(iface,current_ssid):
    iface_metadata = iwlist.scan(iface)
    data = iwlist.parse(iface_metadata)
    foundMalicious = False
    Malicious = []
    for obj in data :
        if(obj['essid'] == current_ssid) :
            Malicious.append(obj)
    
    if len(Malicious)>1:
        print colored("WE FOUND MALICIOUS  CONTENT ON " + iface + "  CHECK YOUR CONNECTIONS NOW !", 'red')
        print colored('\n essid         mac        channel','yellow')
        for obj in Malicious:
            print colored("{}, {}, {}".format(obj['essid'], obj['mac'],obj['channel']),'red')
        print "number of essid with the same name: {}".format(len(Malicious))
    else:
        print colored("Checked! There is no sign of a malicious attack", 'green')


    print ("\n\nscan finished")


def scan_iface():
    os.system('iwconfig')
    i = raw_input("Enter interface name to scan fake content: ")
    essid = raw_input("Enter the current access point name: ")
    os.system('clear')
    print "MALICIOUS SCANNING..."
    detect_malicious_activity(i , essid)



scan_iface()