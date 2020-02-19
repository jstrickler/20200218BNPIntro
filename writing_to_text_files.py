#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]


with open('fruitstuff.txt', 'w') as fruitstuff_out:
    for fruit in fruits:
        line = "{}\t{}\n".format(fruit, len(fruit))
        fruitstuff_out.write(line)
