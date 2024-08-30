class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False

        stack = []
        close = [')', ']', '}']
        dict = {'(': ')', '[': ']', '{': '}'}
        for val in s:
            if val in dict:
                stack.append(val)
            else:
                if len(stack) == 0:
                    return False
                sym = stack.pop()
                if dict[sym] != val:
                    return False
                
        return len(stack) == 0