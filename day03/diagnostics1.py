with open('input.txt', 'r') as fin:
    diags = tuple(map(str.strip, fin.readlines()))

LENGTH = len(diags[0])

bits = [[0, 0] for i in range(LENGTH)]
for i in diags:
    for bit in range(LENGTH):
        if i[bit] == "0":
            bits[bit][0] += 1
        else:
            bits[bit][1] += 1

bits.reverse()
gamma = 0
epsilon = 0
for i in range(len(bits)):
    if bits[i][0] > bits[i][1]:
        epsilon |= 1 << i
    else:
        gamma |= 1 << i

print(epsilon*gamma)
