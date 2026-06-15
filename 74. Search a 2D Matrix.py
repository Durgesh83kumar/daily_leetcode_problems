class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        col = len(matrix[0])

        def binary_search(target, left, right):
            while(left <= right):
                mid = (left+right)//2
                if(matrix[mid//col][mid%col] == target):
                    return True
                elif(matrix[mid//col][mid%col] > target):
                    right = mid-1
                else:
                    left = mid + 1

            return False

        return binary_search(target,0,row*col-1)