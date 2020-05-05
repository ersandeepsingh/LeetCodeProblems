import sys
def maxSubArray(self, nums: List[int]) -> int:
    maxsum = -sys.maxsize
    currsum = -sys.maxsize
    for i in range(len(nums)):
        currsum = max(nums[i], currsum+nums[i] )
        maxsum = max(maxsum, currsum)
    return maxsum