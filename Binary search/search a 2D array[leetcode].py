class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l1 = [ item for elem in matrix for item in elem]
        if target in l1:
            return True
        else:
            return False
        