
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        def search_rec(left, right, up, down):
            if left > right or up > down or target < matrix[up][left] or target > matrix[down][right]:
                return False
            mid = left + (right - left) // 2
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
            return search_rec(left, mid - 1, row, down) or search_rec(mid + 1, right, up, row - 1)

        return search_rec(0, len(matrix[0]) - 1, 0, len(matrix) - 1)

