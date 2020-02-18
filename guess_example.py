#!/usr/bin/env python

max_value = 1000001
min_value = 0

while True:
    guess = (min_value + max_value) // 2

    response = input("Is {} your number? ".format(guess))

    if response == 'q':
        print("Quitter!")
        break

    if response == 'y':
        print("OK! I'm smart!")
        break

    if response == 'h':
        max_value = guess

    if response == 'l':
        min_value = guess
