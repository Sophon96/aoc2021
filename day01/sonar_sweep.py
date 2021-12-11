with open('input.txt', 'r') as fin:
    depths = tuple(map(int, map(str.strip, fin.readlines())))

count = 0
prev = float('inf')
for i in depths:
    if i > prev:
        count += 1
    prev = i

print(count)
