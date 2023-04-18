# 给定一个数组 coordinates ，其中 coordinates[i] = [x, y] ， [x, y] 表示横坐标为 x、纵坐标为 y 的点。
# 请你来判断，这些点是否在该坐标系中属于同一条直线上。

class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates) <= 2:
            return True

        # 计算第一个点与第二个点之间的斜率
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        if x2 - x1 != 0:
            k = (y2 - y1) * 1.0 / (x2 - x1)
        else:
            k = float('inf')

        # 遍历剩余的点，如果斜率不相等，则不在同一条直线上
        for i in range(2, len(coordinates)):
            xi, yi = coordinates[i]
            if xi - x1 != 0:
                if (yi - y1) * 1.0 / (xi - x1) != k:
                    return False
            else:
                if k != float('inf'):
                    return False
        return True