a = 153
num  = a
total = 0

nod = len(str(a))

while num > 0 :
    ld  = num % 10
    # print(ld)
    total = ld ** nod + total
    # print(total)
    num = num // 10

print(total)
if total == a:
    print("armstorn") 
else:
    print("is not")    


    