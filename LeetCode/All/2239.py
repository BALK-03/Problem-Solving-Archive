class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        close = nums[0]
        for number in nums[1:]:
            if abs(close) > abs(number):
                close = number
            elif abs(close) == abs(number):
                if close == number:
                    continue
                close = int(close > number)*close + int(number > close)*number
        return close