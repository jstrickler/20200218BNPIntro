#!/usr/bin/env python

i = 0
while i < 3:
    print(i)
    i += 1
print()

while True:
    animal = input("What is your favorite animal (or q to quit)? ")
    if animal in ('q', 'quit', 'stop'):
    # if animal.startswith('q'):
        break
    if animal == '':  # if not animal:
        continue

    print("OK, you like", animal)

