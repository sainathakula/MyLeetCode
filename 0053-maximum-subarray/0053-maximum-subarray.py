class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ##     kadanes algorithm   ##
        n=len(nums)
        sum1=0
        max1=nums[0]
        i=0
        while(i<n):
            sum1+=nums[i]
            max1=max(max1,sum1)
            if(sum1<0):sum1=0
            i+=1
        return max1
