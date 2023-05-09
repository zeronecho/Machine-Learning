# 给你一个 m x n 的整数网格 accounts ，其中 accounts[i][j] 是第 i位客户在第 j 家银行托管的资产数量。返回最富有客户所拥有的资产总量 。
# 客户的 资产总量 就是他们在各家银行托管的资产数量之和。最富有客户就是 资产总量 最大的客户。


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        row = 0
        totalSums = 0
        while row < len(accounts):
            rowSums = sum(accounts[row])
            if rowSums > totalSums:
                totalSums = rowSums
            row += 1
        return totalSums

    # 官方题解
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))


