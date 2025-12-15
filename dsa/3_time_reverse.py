nums = [1, 2, 3, 4, 5, 6, 7]
k = 3


for _ in range(0, k):
    e = nums.pop()
    nums.insert(0,e)
    
print(nums)