# Jonny Derenge

f = open("day02/day02_input.txt")

lines = f.readlines()
sqfeet = 0


for line in lines:
    len, height, width = [int(i) for i in line.rstrip().split('x')]
    area = len * height * width
    face1, face2, face3 = (len * height), (len * width), (width * height)


    # find smallest face, and add it to area
    if face1 <= face2 and face1 <= face3:
        trim = face1
    elif face2 <= face1 and face2 <= face3:
        trim = face2
    else:
        trim = face3
    area = 2 * (face1 + face2 + face3)
    area = area + trim
    sqfeet = sqfeet + area

print(sqfeet)