#!/usr/bin/env python

s1 = "spam\n"    # \n \r \t \b \f
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"

print("Guido's the man")
print('Guido is the "BDFL" for Python')

print("""Guido's the "BDF" for Python""")

query = """
select * from assets 
where date > '2019-12-01'
order by customer_number
"""
