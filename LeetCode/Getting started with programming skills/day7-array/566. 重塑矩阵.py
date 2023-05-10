# 在 MATLAB 中，有一个非常有用的函数 reshape ，它可以将一个 m x n 矩阵重塑为另一个大小不同（r x c）的新矩阵，但保留其原始数据。
# 给你一个由二维数组 mat 表示的 m x n 矩阵，以及两个正整数 r 和 c ，分别表示想要的重构的矩阵的行数和列数。
# 重构后的矩阵需要将原始矩阵的所有元素以相同的 行遍历顺序 填充。
# 如果具有给定参数的 reshape 操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # 检查是否可重塑
        if r * c != len(mat) * len(mat[0]):
            return mat

        # 将二维列表展平为一维
        flat_list = [num for row in mat for num in row]

        # 创建新矩阵
        new_matrix = []
        for i in range(r):
            row = flat_list[i*c:(i+1)*c]
            new_matrix.append(row)

        return new_matrix

    # # 官方题解：思路很好 值得学习
    # def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
    #     m, n = len(nums), len(nums[0])
    #     if m * n != r * c:
    #         return nums
    #
    #     ans = [[0] * c for _ in range(r)]
    #     for x in range(m * n):
    #         ans[x // c][x % c] = nums[x // n][x % n]
    #
    #     return ans

