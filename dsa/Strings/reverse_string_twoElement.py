# nums = "Vaibhav"
# nums = list(nums)
# print(nums)
# w = 0
# for i in range(0,len(nums)):
#     if i == 1 :
#        temp = nums[i]
#        nums[i] = nums[w]
#        nums[w] = temp
#        w += 1
# print(nums)

num = 'ABCD'
nums = list(num)
m = 0
c = len(nums) - 1 
print(c)
while m < c:
        temp = nums[m]
        nums[m]= nums[c]
        nums[c] = temp
        m = m+1
        c =c- 1
print(nums)


lis  = [1,2,3,4,5]
m = 0
c = len(lis) - 1
while m < c:
        temp = lis[m]
        lis[m] = lis[c]
        lis[c] = temp
        m +=1
        c-=1
print(lis)
