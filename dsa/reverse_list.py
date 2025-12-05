

def vok(ls):
   
    m = 0
    k = []
    all = []
    for i in ls:
       m = i * i 
       k.append(m)
       all.append(i,m)
       
    print(k)
    print(ls[::-1])

        


print(vok(ls = [1,2,3,4,5,6,6]))