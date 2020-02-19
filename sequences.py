#!/usr/bin/python3

ctemps = [-40, 0, 37, 75, 100]

fruits = [
    '    MANGO', 'Apple', '   peach   ', 'PLUM   ', '  Apricot',
    'BaNaNa', 'Persimmon   '
]

for celsius in ctemps:
    fahrenheit = ((9 * celsius)  / 5) + 32

    print("{:8.2f} C is {:8.2f} F".format(celsius, fahrenheit))
print()

clean_fruits = [f.strip().lower() for f in fruits]

print(clean_fruits)

print(" ".join(clean_fruits))

print("/".join(clean_fruits))
