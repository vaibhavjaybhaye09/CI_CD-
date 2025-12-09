num = [1, 3, 1, 4, 4, 2, 5, 5, 5]
c = 0
for i in range(0,len(num) - 1):
        for j in range(i + 1, len(num)):
                if num[i] == num[j - 2]:
                        c +=1
        

print(c)
                        
