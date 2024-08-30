class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        left, right = 0, len(s) - 1

        while left <= right:
            if not (('a' <= s[left] <= 'z') or ('0' <= s[left] <= '9')):
                left += 1
                continue
            
            if not (('a' <= s[right] <= 'z') or ('0' <= s[right] <= '9')):
                right -= 1
                continue
            
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True