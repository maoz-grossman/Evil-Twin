import os

def Change_to_MonitorMode(iface):
    os.system("sudo airmon-ng check kill")
    os.system("sudo airmon-ng start "+ iface)
    os.system("clear")
    iface = str(iface)+'mon'
    return iface

def change_to_MonitorMode(iface):
    os.system("sudo ip link set "+ iface+ " down")
    os.system("sudo iw"+ iface+  " set monitor none")
    os.system("sudo ip link set "+ iface+ " down")
    os.system("clear")

def change_back(iface):
    os.system("sudo ip link set "+ iface+ " down")
    os.system("sudo iw"+ iface+  " set type managed")
    os.system("sudo ip link set "+ iface+ " down")


def Change_back(iface):
    os.system("sudo airmon-ng stop "+ iface)
    os.system("sudo systemctl start NetworkManager")
    os.system("clear")
