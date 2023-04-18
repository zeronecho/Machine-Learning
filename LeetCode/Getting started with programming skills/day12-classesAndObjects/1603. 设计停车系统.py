# https://leetcode.cn/problems/design-parking-system/?envType=study-plan&id=programming-skills-beginner&plan=programming-skills&plan_progress=x5t930sg

# 请你给一个停车场设计一个停车系统。停车场总共有三种不同大小的车位：大，中和小，每种尺寸分别有固定数目的车位。
#
# 请你实现 ParkingSystem 类：
#
# ParkingSystem(int big, int medium, int small) 初始化 ParkingSystem 类，三个参数分别对应每种停车位的数目。
# bool addCar(int carType) 检查是否有 carType 对应的停车位。 carType 有三种类型：大，中，小，分别用数字 1， 2 和 3 表示。一辆车只能停在  carType 对应尺寸的停车位中。如果没有空车位，请返回 false ，否则将该车停入车位并返回 true 。

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spots = [big, medium, small]  # 用一个列表记录每种尺寸停车位的数目

    def addCar(self, carType: int) -> bool:
        if self.spots[carType - 1] > 0:  # 检查对应尺寸的停车位是否有空位
            self.spots[carType - 1] -= 1  # 有空位则将该停车位数目减1
            return True
        else:
            return False

# 这段代码使用了一个列表来记录停车场中每种尺寸停车位的数目，在初始化时传入三种尺寸停车位的总数。
# addCar方法接收一个carType参数，表示车辆的尺寸，根据车辆尺寸在列表中对应的位置减1，如果该位置的停车位数目大于0，说明有空位可以停车，返回True，否则返回False。