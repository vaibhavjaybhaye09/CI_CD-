

class solution:
    def sol(self,nums):
        w = 0
        for i in range(len(nums)):
            if nums[i] != 4:
                nums[i], nums[w] = nums[w], nums[i]
                w += 1
        return nums


nums = [2,4,4,335,0,56,43,0]
d = solution()
print(d.sol(nums))