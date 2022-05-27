f = open("day01_input.txt")

lines = f.readlines()
pos = 0
for line in lines:
    for character in line:
        if character == '(':
            pos = pos + 1
        else:
            pos = pos -1


print(pos)