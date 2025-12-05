
class Solution:
    def sol(self,digits):        
        max_d = max(digits)
        ind = digits.index(max_d)
        
        digits[ind] = max_d + 1
        digits = list(map(int,str(ind)))
        
        return digits 

digits = [9]

d = Solution()
print(d.sol(digits))