'''
https://leetcode.com/problems/design-parking-system/

Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.

Implement the ParkingSystem class:

ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class. The number of slots for each parking space are given as part of the constructor.
bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get into the parking lot. carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively. A car can only park in a parking space of its carType. If there is no space available, return false, else park the car in that size space and return true.

'''


class ParkingSystem(object):

    def __init__(self, big, medium, small):
        #We store the parking space available for each car category in the respective variable
        self.big = big
        self.medium = medium 
        self.small = small

    def addCar(self, carType):
        #checking if the incoming car is big and if parking space is available for big cars
        if carType == 1 and self.big > 0:
            self.big -=1
            return True
        #checking if the incoming car is medium and if parking space is available for medium cars
        elif carType == 2 and self.medium > 0:
            self.medium -=1
            return True 
        #checking if the incoming car is small and if parking space is available for small cars
        elif carType == 3 and self.small > 0:
            self.small -=1
            return True
        #If the car isnt either small,medium,big or if the parking space isnt available then we return false
        else:
            return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
