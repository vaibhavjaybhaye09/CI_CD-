class Solution:
    def sol(self,num):
        n = []
        for i in range(1, 20):
            if num % i == 0:
                n.append(i)

        return n
                


d = Solution()
print(d.sol(20))
 