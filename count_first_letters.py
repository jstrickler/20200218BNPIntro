#!/usr/bin/env python

letter_counts = {}

with open('DATA/words.txt') as words_in:
    for word in words_in:
        first = word[0]
        if first in letter_counts:
            letter_counts[first] = letter_counts[first] + 1
            # letter_counts[first] += 1
        else:
            letter_counts[first] = 1

for wombat, umbrella in letter_counts.items():
    print(wombat, umbrella)


x = [10, 20, 30]

for i in x:
    #  i = next(x)
    print(i)
