# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
            
        s, f = 0, n-1
        while s <= f:
            if not isBadVersion(s+1):
                mid = s + (f - s) // 2
                if not isBadVersion(mid+1):
                    s = mid + 1
                else:
                    f = mid
            else:
                return s+1