import os
import signal
import time

dnsmasq_conf = "dnsmasq.conf"
hostapd_conf = "hostapd.conf"

def kill_dnsmasq_and_hostapd():
	os.system("killall dnsmasq hostapd")

def start_dnsmasq(iface):
	os.system("dnsmasq -C " + dnsmasq_conf)
	os.system("iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE")
	os.system("iptables -A FORWARD -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT")
	os.system("iptables -A FORWARD -i " + iface + " -o eth0 -j ACCEPT")
	os.system("sysctl -w net.ipv4.ip_forward=1")


def restart_network():
	os.system("service network-manager restart")	

def start(iface):
    kill_dnsmasq_and_hostapd()
    start_dnsmasq(iface)
    print("\npress CTRL + C  twice to stop\n")
    while True:
        try:
            time.sleep(1)
            os.system("hostapd " + hostapd_conf)
        except KeyboardInterrupt:
            break
	
	