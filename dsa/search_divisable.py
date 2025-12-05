

class solution:
   
    def sol(self,nums):
        num = 20
        s = []
        for i in nums:
            if num % i == 0:
                s.append(i)
        return s
        
    





nums = [11, 2, 34, 3, 546, 56, 676, 34, 5, 4, 6]
d = solution()
print(d.sol(nums))