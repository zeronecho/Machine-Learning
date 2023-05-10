# 给你一个正方形矩阵 mat，请你返回矩阵对角线元素的和。
# 请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。

class Solution:

    def diagonalSum(self, mat: List[List[int]]) -> int:
        sums = 0
        n = len(mat)
        for i in range(n):
            sums += mat[i][i] + mat[i][n - i - 1]
        if n % 2 != 0:
            sums -= mat[n // 2][n // 2]
        return sums


    # # 官方题解
    # def diagonalSum(self, mat: List[List[int]]) -> int:
    #     n = len(mat)
    #     return sum(mat[i][j] for i in range(n) for j in range(n) if i == j or i + j == n - 1)
