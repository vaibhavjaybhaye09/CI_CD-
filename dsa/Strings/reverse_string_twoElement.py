nums = "Vaibhav"
nums = list(nums)
print(nums)
w = 0
for i in range(0,len(nums)):
    if i == 1 :
       temp = nums[i]
       nums[i] = nums[w]
       nums[w] = temp
       w += 1
print(nums)