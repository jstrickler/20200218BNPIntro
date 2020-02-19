#!/usr/bin/env python

d1 = dict() # new, empty, dictionary
capitals = {'NY': 'Albany', 'NC': 'Raleigh', 'CT': 'Hartford', 'NJ': 'Trenton'}

print(capitals['NY'])
print(capitals['NJ'])

capitals['PA'] = 'Harrisburg'
print(capitals)

capitals['NC'] = 'Durham'
print(capitals)

print(capitals.get('CA'))
print(capitals.get('CA', 'NOT FOUND'))
print(capitals.get('CT', 'NOT FOUND'))

print(capitals.keys())
print(capitals.values())

print(len(capitals))

for k in 'NC', 'NY', 'NM', 'MN', 'CT':
    print(k, k in capitals)  # is it a key?
print()

# for k, v in D.items()
for state, capital in capitals.items():
    print(state, capital)
print()

for state, capital in sorted(capitals.items()):
    print(state, capital)
print()

capitals["MA"] = "Boston"
print(capitals)




