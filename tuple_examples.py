#!/usr/bin/env python

person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'

print(person[0], person[1])

print(person[:2])

first_name, last_name, product, dob = person  # iterable unpacking


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

print(people[0])
print(people[0][0])
print(people[0][0][0])
print()

for person in people:
    # person = get next element of people
    print(person)
print()



place = "Manhattan", "New York", "NY"

borough, city, state = place
# borough = place[0]
# city = place[1]
# state = place[2]


values = ['a', 'b', 'c', 'd', 'e', 'f']

x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)


for person in people:
    first_name, last_name, product, dob = person
    # first_name, last_name, product, dob = get next element of people:
    print(first_name, last_name)


t = 1, 5, "wombat"

tlist = list(t)

print(t)
print(tlist)
tlist.append("cobra")
print(tlist)
