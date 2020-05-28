class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if(nums[i]==1):
                continue
            nums[i]=-1
        d= {} 
        max_len=0
        curr_sum=0
        for i in range(len(nums)): 
            curr_sum += nums[i] 
            if nums[i] is 0 and max_len is 0: 
                max_len = 1
            if curr_sum is 0: 
                max_len = i + 1
            if curr_sum in d: 
                max_len = max(max_len, i-d[curr_sum]) 
            else: 
                d[curr_sum] = i 
        return max_len
