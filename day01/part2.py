with open('input.txt', 'r') as fin:
    depths = tuple(map(int, map(str.strip, fin.readlines())))

count = 0
prev = sum(depths[0:3])
for i in range(1, len(depths)-2):
    cur = prev-depths[i-1]+depths[i+2]
    if cur > prev:
        count += 1
    prev = cur

print(count)
