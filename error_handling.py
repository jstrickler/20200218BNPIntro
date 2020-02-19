#!/usr/bin/env python

try:
    with open('DATA/wombatfactory.txt') as wf_in:
        pass  # do nothing much
except Exception as err:
    print(err)

print("Splendid!")


try:
    stuff = ['a', 'b', 'c', 'd', 'e', 'f']
    print(stuff[19])
except IndexError as err:
    print(err)


for value in 8, 0, 19, "12", -4, 5:
    try:
        result = 27 / value
    except ZeroDivisionError as err:
        print(err)
    except TypeError as err:
        print(err)
    else:
        print(result)



