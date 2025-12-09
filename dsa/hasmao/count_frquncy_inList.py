num = [ 1, 2, 3, 4, 5, 5, 3, 34, 4]

n = num
frequency_map = dict()

for i in range(0 ,len(n)):
    if num[i] in frequency_map:
        frequency_map[num[i]] += 1
    else:
        frequency_map[num[i]] = 1


print(frequency_map[num[5]])

        