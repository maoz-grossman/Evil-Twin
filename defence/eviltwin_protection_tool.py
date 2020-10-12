import os
import iwlist
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


def detect_malicious_activity(iface):
    iface_metadata = iwlist.scan(iface)
    data = iwlist.parse(iface_metadata)

    for obj in data :
        if(data.count(obj['mac']) > 1 and data.count(obj['essid']) > 1):
            print("WE FOUND MALICIOUS  CONTENT ON " + iface + "  CHECK YOUR CONNECTIONS NOW !\n")

    print ("scan finished")


def scan_iface():
    i = raw_input("Enter interface name to scan fake content: ")
    detect_malicious_activity(i)




scan_iface()