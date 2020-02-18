#!/usr/bin/env python
import sys

raw_celsius = sys.argv[1]

celsius = float(raw_celsius)

fahrenheit = ((9 * celsius)  / 5) + 32

print("{:.2f} C is {:.2f} F".format(celsius, fahrenheit))


