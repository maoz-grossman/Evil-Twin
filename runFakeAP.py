import FakeAP as f_ap
import os
import sys

def run():
    i = raw_input("Enter interface name: ")
    type(i)
    f_ap.start(str(i))

run()