class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = sum([int(digit)**2 for digit in str(n)])
        
        if n == 1:
            return True
        elif n in seen:
            return False