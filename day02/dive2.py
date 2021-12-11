with open('input.txt', 'r') as fin:
    instructions = tuple(map(str.split, fin.readlines()))

depth = 0
horiz = 0
aim = 0
for i in instructions:
    if i[0] == 'forward':
        horiz += int(i[1])
        depth += int(i[1])*aim
    elif i[0] == 'down':
        aim += int(i[1])
    elif i[0] == 'up':
        aim -= int(i[1])
    else:
        print('what')
        exit(1)

print(depth, horiz)
print(depth*horiz)
