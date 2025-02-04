class Solution:
    def maximumGap(self, nums) -> int:

        nums.sort()
        max_gap=0

        for i in range(len(nums)-1):
            
              gap=nums[i+1] - nums[i]
              if gap > max_gap:
                   max_gap=gap

        return max_gap




s1 =Solution()
print(s1.maximumGap([3,6,9,1]))