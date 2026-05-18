n  = 2201
num = n
m = 0
c = len(str(num))- 1
while m > c :
    temp = num[m]
    num[m]= num[c]
    num[c] = temp
    m = m+1
    c= c-1
    print("".join(num))


