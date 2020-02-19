#!/usr/bin/env python

with open("DATA/mary.txt") as weasel:
    for raw_line in weasel:
        line = raw_line.rstrip()
        print(line)  # , repr(line))
print('-' * 60)

with open("DATA/mary.txt") as weasel:
    contents = weasel.read()
    print("RAW CONTENTS:")
    print(repr(contents), '\n')
    print("CONTENTS:")
    print(contents)
print('-' * 60)

with open("DATA/mary.txt") as weasel:
    all_lines = weasel.readlines()
    print("all lines:", all_lines)

