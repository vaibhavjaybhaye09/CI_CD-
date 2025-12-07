


class Solution:
    def removeDuplicates(self, nums):
        r=2
        w=2
        while r<len(nums):
            if not(nums[w-2]==nums[w-1]==nums[r]):
                nums[w]=nums[r]
                w+=1
            r+=1
        return w
    
nums = [1, 2, 2, 2, 3, 4, 5]

d = Solution()
print(d.removeDuplicates(nums))