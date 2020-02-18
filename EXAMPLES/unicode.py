#!/usr/bin/env python

print('26\u00B0')  # <1>
print('26\N{DEGREE SIGN}')  # <2>
print(r'26\u00B0\n')  # <3>
print()

print('we spent \u20ac1.23M for an original C\u00e9zanne') # <4>
print("Romance in F\u266F Major")
print()

#      list
data = ['\U0001F95A', '\U0001F414'] # <5>
print(sorted(data))

print("This class makes my \U0001F92F")

actor = "Chris Hemsworth"

print(len(actor))

print(actor.upper())

ch = actor.upper()

print(ch)

names = actor.split()
print(names)

print(actor.lower())

print(actor.count('h'))
print(actor.count('worth'))
m = "Mississippi"
print(m.count('iss'))
print(actor.lower().count('h'))
print(actor.count('h') + actor.count('H'))

s = "New York:NY:USA"
print("NY Split", s.split(':'))
s = "Twas brillig an the slithy toves did gyre and gimbal in the wabe"

print("Lewis Carroll split", s.split())

s = "Thisisatest"

s = "      I Love wombats!       "

print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()


s = "wvowvoovwwwwwvvvowwI Love wombats!vowvowwovwovooovvvwwwvwo"

print("|" + s.lstrip("wvo") + "|")
print("|" + s.rstrip("wvo") + "|")
print("|" + s.strip("wvo") + "|")
print()

print(s.replace('w', '').replace('v', '').replace('o', ''))

print(actor.replace('Chris', 'Liam'))
print(actor.replace('Chris ', ''))


s = "foofoofoobar"

print(s.replace("foo", ""))
print(s.replace("foo", "", 1))









