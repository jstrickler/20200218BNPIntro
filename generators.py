#!/usr/bin/env python

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]
print(len(nums), min(nums), max(nums), sum(nums))

print(sorted(nums))

rnums = reversed(nums)

for i in rnums:
    print(i, end=' ')
print('\n')

rnums = reversed(nums)
print(rnums)

cities = ["New York", "Durham", "Houston"]
states = ['NY', 'NC', 'TX', 'MN', 'ME', 'MO']

places = zip(cities, states)
print(places)

print(list(places), '\n')

places = zip(cities, states)
for p in places:
    print(p)
print()

places = zip(cities, states)
for city, state in places:
    print("{}, {}".format(city, state))
print()

for city in cities:
    print(city)
print()


print(list(enumerate(cities)), '\n')

for i, city in enumerate(cities, 1):
    print(i, city)
print()

print(cities + states)
print(cities * 3)
print([True] * 5)

values = [0] * 100
print(values, '\n')


for i in range(10):
    print(i)
print()
# range(STOP)  range(START, STOP)  range(START, STOP, STEP)

for i in range(1, 11):
    print(i)
print()

for i in range(5, 101, 5):
    print(i, end=' ')
print('\n')



