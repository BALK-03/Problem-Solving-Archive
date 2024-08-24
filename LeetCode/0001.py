class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dict:
                return [dict[diff], i]
            dict[nums[i]] = i