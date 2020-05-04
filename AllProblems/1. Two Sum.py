class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        for i in range(len(nums)):
            second = target - nums[i]
            if second in diff_dict:
                return (list([i, diff_dict[second]]))
            else:
                 diff_dict[nums[i]] = i