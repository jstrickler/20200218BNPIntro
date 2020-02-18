#!/usr/bin/env python

list1 = list()  # empty list
cities = ["Rye", "NYC", "Albany", "Troy"]
list2 = []  # empty list

colors = "red black green purple yellow".split()
print(colors)
print()

print(cities)
cities.append("Buffalo")
cities.append("Syracuse")
print(cities)

more_cities = ["Rochester", "Poughkeepsie", "Schenectady"]
cities.extend(more_cities)

cities[0] = "New Rochelle"

print(cities)

cities.insert(0, "Elmira")
cities.insert(5, "Corning")
print(cities)

del cities[0]

print(cities)

cities.remove('Syracuse')

print(cities)

c = cities.pop()
print(c)
print(cities)
c = cities.pop(4)
print(c)
print(cities)

print(cities[0])
print(cities[3])
print(cities[6])
print(cities[-1])
print(cities[len(cities)-1])


fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

print(fruits[0], fruits[1], fruits[-2], fruits[-1])

#  S[START:STOP]  s[:STOP]  s[START:]  s[START:STOP:STEP]

print(fruits[0:5])
print(fruits[:5])
print(fruits[4:12])
print(fruits[19:])
print(fruits[-5:])

fruits.sort(reverse=True)
print(fruits)
print(fruits[0:5])
print(fruits[:5])
print(fruits[4:12])
print(fruits[19:])
print(fruits[-5:])

actor = 'Chris Hemsworth'

print(actor[:5])
print(actor[-9:])

print(actor[6:10])
print('-' * 60)

for city in cities:
    print(city)
print()

for chr in "do re me":
    print(chr)
print()

for fruit in fruits[:10]:
    print(fruit)

