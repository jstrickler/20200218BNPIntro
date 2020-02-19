#!/usr/bin/env python
from pprint import pprint

president_names = []
with open('DATA/presidents.txt') as pres_in:
    for raw_line in pres_in:  # for each line in file
        line = raw_line.rstrip() # remove \n
        term, first_name, last_name, date_born, date_died, birth_place, birth_state, took_office, left_office, party = line.split(':')
        president_names.append((first_name, last_name, party))

pprint(president_names)
