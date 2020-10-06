from configparser import ConfigParser

def Create_hostapd(iface, ssid="Free wifi"):
    config_object = ConfigParser()
    config_object["HOSTAPD"] = {
    "interface": iface ,
    "driver" : "nl80211",
    "ssid" : ssid ,
    "channel": 1
    }

    interface_str= "interface="+iface+"\n"
    driver_str="driver=nl80211\n"
    ssid_str= "ssid="+ssid+"\n"
    channel_str = "channel=1\n"
    conf_str= interface_str+driver_str+ssid_str+channel_str
    f = open("hostapd.conf", "w")
    f.write(conf_str)
    #with open('hostapd.conf', 'w') as conf:
        #config_object.write(conf)

