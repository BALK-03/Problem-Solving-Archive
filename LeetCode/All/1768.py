# FIRST SOLUTION
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = ''
        w1_flag, w2_flag = False, False
        i = 0
        while i < min(len(word1), len(word2)):
            if not w1_flag:
                merged += word1[i]
                w1_flag = True
                continue
            elif not w2_flag:
                merged += word2[i]
                w2_flag = True
                continue
            else:
                i += 1
                w1_flag, w2_flag = False, False
        if i == len(word1):
            merged += word2[i:]
        else:
            merged += word1[i:]
        return merged


# SECOND SOLUTION
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = ''
        p1, p2 = 0, 0

        while p1<len(word1) and p2<len(word2):
            merged += word1[p1] + word2[p2]
            p1 += 1
            p2 += 1
        
        if p1 == len(word1) and p2 == len(word2):
            return merged
        elif p1 == len(word1) and p2 < len(word2):
            return merged + word2[p2:]
        elif p1 < len(word1) and p2 == len(word2):
            return merged + word1[p1:]