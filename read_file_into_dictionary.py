#!/usr/bin/env python
from pprint import pprint

knight_info = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')

        knight_info[name] = title, color, quest, comment

pprint(knight_info)
print()

for knight, data in knight_info.items():
    print(data[0], knight)
print()

print(knight_info['Robin'][2])
