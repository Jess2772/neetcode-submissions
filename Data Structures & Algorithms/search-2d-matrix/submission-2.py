class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # cant you somehow compress this into a 1D array? 
        # think of it as a 2d array.
        m = len(matrix)
        n = len(matrix[0])
        mn = m * n

        l, r = 0, mn - 1

        while l <= r:
            mid = (l + r) // 2
            nr = mid // n
            nc = mid % n
            if matrix[nr][nc] == target:
                return True
            elif matrix[nr][nc] < target:
                l = mid + 1
            else:
                r = mid - 1
            
        return False
        