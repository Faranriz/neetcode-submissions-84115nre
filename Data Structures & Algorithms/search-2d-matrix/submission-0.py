class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binary_search(matrix_row: List[int]):
            l, r = 0, len(matrix_row) - 1
            while l <= r:
                mid = (l + r) // 2
                if matrix_row[mid] == target:
                    return True
                elif matrix_row[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False


        l_row, r_row = 0, len(matrix) - 1
        while l_row <= r_row:
            mid_row = (l_row + r_row) // 2
            if matrix[mid_row][0] <= target and matrix[mid_row][-1] >= target:
                return binary_search(matrix[mid_row])
            elif matrix[mid_row][0] > target:
                r_row = mid_row - 1
            else:
                l_row = mid_row + 1

        return False
