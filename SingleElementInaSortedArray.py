class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for j in range(1,len(nums),2):
            if(nums[j-1]==nums[j]):
                continue
            else:
                return nums[j-1]
        return nums[-1]
