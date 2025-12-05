
class Solution:
    def sol(self,digits):        
        max_d = max(digits)
        ind = digits.index(max_d)

        digits[ind] = max_d + 1
              
        return digits 

digits = [1, 2, 3, 5]

d = Solution()
print(d.sol(digits))