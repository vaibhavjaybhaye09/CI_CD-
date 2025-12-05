ls = [4, 3, 2, 1]
e = len(ls)
print(e)
max_d = max(ls)
inde = ls.index(max_d)
ls[inde] = max_d + 1

min_n = min(ls)
min_index = ls.index(min_n)
ls[min_index] = min_n + 1

if e == 1 :
    num = ls
    max_o = max(num)
    num  = list(map(int, str(max_o)))
    print(num)
else:
    print(ls)


# ls = list(map(int,str(ind))) 
