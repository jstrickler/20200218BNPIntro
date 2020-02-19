#!/usr/bin/env python

shell_counts = {}

with open('DATA/passwd') as passwd_in:
    for raw_line in passwd_in:
        line = raw_line.rstrip()
        login, uid, gid, pw, comment, home, shell = line.split(':')
        # fields = line.split(':')
        # shell = fields[-1]
        if shell == '':
            shell = 'NONE'

        if shell in shell_counts:
            shell_counts[shell] += 1
        else:
            shell_counts[shell] = 1

for shell, count in shell_counts.items():
    print(shell, count)
