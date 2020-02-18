#!/usr/bin/env python

while True:
    raw_celsius = input("Enter temp in C: ")
    if raw_celsius == "q":
        print("bye!")
        break
    if raw_celsius == '':
        continue

    celsius = float(raw_celsius)
    fahrenheit = ((9 * celsius) / 5) + 32

    print("{:.2f} C is {:.2f} F".format(celsius, fahrenheit))
