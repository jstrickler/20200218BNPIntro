#!/usr/bin/env python

with open('DATA/mary.txt') as mary_in:
    with open('betsy.txt', 'w') as betsy_out:
        with open('bob.txt', 'w') as bob_out:
            for line in mary_in:
                betsy_data = line.replace('Mary', 'Betsy')
                betsy_out.write(betsy_data)

                bob_data = line.replace('Mary', 'Bob')
                bob_out.write(bob_data)
