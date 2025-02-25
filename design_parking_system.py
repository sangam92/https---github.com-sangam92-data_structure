"""
Design Parking System

"""

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big=big
        self.medium=medium
        self.small=small
        

    def addCar(self, carType: int) -> bool:
        res=[]
        res.append(None)
        if carType==1 and self.big>0:
            self.big-=1
            res.append(True)
        else:
            res.append(False)

        if carType==2 and self.medium>0:
            self.medium-=1
            res.append(True)
        else:
            res.append(False) 

        if carType==3 and self.small>0:
            self.small-=1
            res.append(True)
        else:
            res.append(False)        


        return res
            
        
obj = ParkingSystem(1, 1, 0)
param_1 = obj.addCar(1)
param_2 = obj.addCar(2)
param_3 = obj.addCar(3)
param_4 = obj.addCar(1)

print(param_4)