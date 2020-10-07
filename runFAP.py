import FakeAP as f_ap
import os
import sys

def fun():
    i = input("Enter interface name: ")
    type(i)
    f_ap.start(str(i))

fun()