digits = [9]
num = [int("".join(map(str, digits)))]
for i in num:
    digit = i + 1
    break
num = list(map(int,str(digit)))
print(num)



