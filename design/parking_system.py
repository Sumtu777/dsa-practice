# Design Parking System: https://leetcode.com/problems/design-parking-system/
# Pattern: design (classes)
# Time: O(1) per addCar   Space: O(1)

# First Try 

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.size = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.size[0] >0:
            self.size[0]-=1
            return True
        if carType == 2 and self.size[1] >0:
            self.size[1]-=1
            return True
        if carType == 3 and self.size[2] >0:
            self.size[2]-=1
            return True
        
        return False

## second try 

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.size = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        i = carType -1
        if self.size[i] > 0:
            self.size[i] -= 1
            return True

        
        return False