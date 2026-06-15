http://leetcode.com/problems/rotate-image/


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            s = 0
            e = len(matrix[i])-1
            while(s<e):
                matrix[i][s], matrix[i][e] = matrix[i][e],matrix[i][s]
                s += 1
                e -= 1

        return matrix