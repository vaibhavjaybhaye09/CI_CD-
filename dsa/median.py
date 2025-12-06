class Solution:
    def sol(self,nums1,nums2):
        merge_list = sorted(nums1+nums2)
        print(merge_list)
        length = len(merge_list)  

        if length % 2 == 0:
           mid1 = merge_list[(length // 2) - 1]
           mid2 = merge_list[(length // 2)]
           sum_ofmedian  = mid1 + mid2
           return f'{sum_ofmedian / 2:.4f}'
        else:          
            mid2 = merge_list[(length // 2)]
            return f"{mid2 / 2:.4f}"

    

nums1 = [1, 2, 3]
nums2 = [6, 7, 9]
ans = Solution()
print(ans.sol(nums1,nums2))


