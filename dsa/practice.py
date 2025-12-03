n = 1111

num = n

def ok(num):
    original = 0 

    while num > 0 :
        lsd =  num % 10
        original = (original * 10) + lsd
        num = num % 10

    return original == num


# print(ok(num))
        
def vs(st):
    rev = ""
    st = st.replace(" ","")
    for i in st:
        rev = i + rev
    return rev


print(vs("vaibhav pratiksha"))