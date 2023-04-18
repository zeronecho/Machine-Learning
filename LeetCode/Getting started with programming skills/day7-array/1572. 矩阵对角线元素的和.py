# https://leetcode.cn/problems/matrix-diagonal-sum/?envType=study-plan&id=programming-skills-beginner&plan=programming-skills&plan_progress=x5t930sg

# 给你一个正方形矩阵 mat，请你返回矩阵对角线元素的和。
# 请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        return sum(mat[i][j] for i in range(n) for j in range(n) \
                    if i == j or i + j == n - 1)
