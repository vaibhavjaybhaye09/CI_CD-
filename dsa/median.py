class Solution:
    def sol(self,nums1,nums2):
        arr = nums1 + nums2
        arr.sort()
        m = len(arr)

        if m % 2 == 0:
            return (arr[m // 2 -1] + arr[m // 2]) / 2
        else:
            return arr[m // 2]

    

nums1 = [1, 2]
nums2 = [3]
ans = Solution()
print(ans.sol(nums1,nums2))


