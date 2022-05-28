# Jonny Derenge
from enum import unique

f = open("day03/day03_input.txt")

lines = f.readlines()
coord = [(0,0)]

for line in lines:
    counter = 0
    for character in line:
        if character == '<':
            coord.append((coord[-1][0] -1, coord[-1][1]))
        elif character == '>':
            coord.append((coord[-1][0] +1, coord[-1][1]))
        elif character == '^':
            coord.append((coord[-1][0], coord[-1][1] +1))
        else:
            coord.append((coord[-1][0], coord[-1][1] -1))
        counter += 1

unique = len(list(set(coord)))
print(unique)