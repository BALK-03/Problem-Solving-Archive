class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        sr, er = 0, len(matrix)-1
        while sr <= er:
            mr = sr + (er - sr) // 2
            if not matrix[mr][0] <= target <= matrix[mr][-1]:
                if sr == er:
                    return False
                if target < matrix[mr][0]:
                    er = mr - 1
                elif target > matrix[mr][-1]:
                    sr = mr + 1
            else:
                break
        
        sc, ec = 0, len(matrix[0])-1
        while sc <= ec:
            mc = sc + (ec - sc) // 2
            if matrix[mr][mc] == target:
                return True
            elif matrix[mr][mc] > target:
                ec = mc - 1
            else:
                sc = mc + 1
        return False