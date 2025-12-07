num1 = [1, 2, 3, 0, 0, 0]
num2 = [2, 4, 5]
m = 3
n = 3

i = m - 1      # last element of real nums1 part
j = n - 1      # last element of nums2
k = m + n - 1  # last index of nums1

while j >= 0:
    if i >= 0 and num1[i] > num2[j]:
        num1[k] = num1[i]
        i -= 1
    else:
        num1[k] = num2[j]
        j -= 1
    k -= 1

print(num1)

# num = num1 + num2
# result = [x for x in num if x != 0]

# print(sorted(result))