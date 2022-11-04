from time import time, sleep
from itertools import product
from numpy import loadtxt
import re

with open("D:/CyberS/5/4DigitPinSortedByFrequency.txt") as file_in:
    common_pin = []
    common_pin_frequency = []
    for line in file_in:
        res = line.split(',', 1)
        common_pin.append(res[0])
        common_pin_frequency.append(res[1])

pin = input("Enter Pin : ")

if pin in common_pin:
   i=common_pin_frequency[(common_pin.index(pin))]
   print(f"frequency score (out of 255) = ",i)
   print("Higher the score, more common the pin is")
   


else:
    print("Pin not found.")

