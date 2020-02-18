#!/usr/bin/env python

raw_celsius = input("Enter temp in C: ")

celsius = float(raw_celsius)

fahrenheit = ((9 * celsius)  / 5) + 32

print("{:.2f} C is {:.2f} F".format(celsius, fahrenheit))


