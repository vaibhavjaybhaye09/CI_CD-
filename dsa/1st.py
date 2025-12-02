# reverse varaible without using reverse function palindrome

n = 1111

num = n

# def reve(num):
#     result = 0
#     while num > 0 :
#         lsd = num % 10
#         result = (result * 10) + lsd
#         num = num // 10
#     return n == result

# print(reve(num))

def ok(num):
    print(type(num))
    original = 0
    while num > 0:
        lsd = num % 10
        original = (original * 10) + lsd
        num = num // 10
    return original == n

print(ok(num))



