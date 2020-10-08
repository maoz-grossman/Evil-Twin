import os 

def Create_hostapd(iface, ssid="Free wifi"):
    interface_str= "interface="+str(iface)+"\n"
    driver_str="driver=nl80211\n"
    ssid_str= "ssid="+str(ssid)+"\n"
    channel_str = "channel=1 \n"
    conf_str= interface_str+driver_str+ssid_str+channel_str
    f = open("hostapd.conf", "w+")
    f.write(conf_str)
    os.chmod("hostapd.conf",0o777)


def Create_dnsmasq(iface):
    iface_str= "interface="+str(iface)+""
    body_str= "\ndhcp-range=10.0.0.3,10.0.0.20,12h"
    body_str+="\ndhcp-option=3,10.0.0.1"
    body_str+="\ndhcp-option=6,10.0.0.1"
    body_str+="\naddress=/#/10.0.0.1"
    conf_str = iface_str+body_str
    f = open("dnsmasq.conf", "w+")
    f.write(conf_str)
    os.chmod("dnsmasq.conf",0o777)


def Delete_conf_files():
    os.system("rm *.conf")