#!/usr/bin/env python
a = "wombat"
b = 23.3902393
c = "Chris Hemsworth"

print(a, b, c)
print("Actor", c, 1234)

print(a, b, c, sep="//")

print(a, b, c, end="&")
print("Continuing....")

print(b)

print("value is {}".format(b))

country = "Australia"

print("{} is from {}".format(c, country))

print("value is {:.1f}".format(b))

print(f"{c} is from {country}")

x = "value is {:.1f}".format(b)

print(x)


x = f"value is {b:.1f}"
print(x)

#  "  "   r"  "   f"   "

big_num = 23529385023958203985209835

print("{:,d}".format(big_num))

