class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0

        s = set(nums)
        longest = 0
        for num in s:
            if num - 1 not in s:
                next = num + 1
                length = 1
                while next in s:
                    length += 1
                    next += 1
                longest = max(length, longest)
            
        return longest