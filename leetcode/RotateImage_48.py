from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        t = [[0 for _ in range(c)] for _ in range(r)]

        for i in range(r):
            for j in range(c):
                t[j][r - 1 - i] = matrix[i][j]

        for i in range(r):
            for j in range(c):
                matrix[i][j] = t[i][j]
                print(matrix[i][j], "\t" , end='')
            print("\n")

x = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
x.rotate(matrix)


