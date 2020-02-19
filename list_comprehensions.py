#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

f1 = [f.upper() for f in fruits]
print("orig:", fruits)
print("f1:", f1, '\n')

#  [EXPR-TO-ADD for VARIABLE in ITERABLE]

f2 = [f[:3] for f in fruits]
print("f2:", f2, '\n')

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n1 = [n * 2.0 for n in sorted(nums)]
print("n1:", n1, '\n')

f3 = [(f, f.upper()) for f in fruits]
print("f3:", f3, '\n')

for orig, new in zip(fruits, f1):
    print(orig, new)
print("\n")

f4 = [f.upper() for f in fruits if f.startswith('p')]
print("f4:", f4, '\n')

f5 = [f for f in fruits if f.startswith('p')]
print("f5:", f5, '\n')

raw_food = ["spam", "spam", "spam", "spam", "spam", "toast", "spam",
            "ham", "spam", "spam", "spam", "spam", "spam", "spam",
            "spam", "eggs", "eggs", "bacon", "spam", "spam", "spam", "spam", ]

food = [f for f in raw_food if not f == 'spam']
print("food:", food, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

last_names = [p[1] for p in people]
print("last names:", last_names, '\n')

dobs = [p[3] for p in people]
print("DOBs:", dobs, '\n')

fgen = (f.upper() for f in fruits)
print(fgen, '\n')

for fruit in fgen:
    print(fruit)
print()

