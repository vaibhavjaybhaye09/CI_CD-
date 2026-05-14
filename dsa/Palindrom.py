n = 121
num = n
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if n == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")