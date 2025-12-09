num = [ 1, 2, 3, 4, 5, 5, 3, 34, 4]

n = num
freq_map = dict()

for i in range(0, len(n)):
    if num[i] in freq_map:
        freq_map[num[i]] += 1
    else:
        freq_map[num[i]] = 1


print(freq_map[num[3]])
