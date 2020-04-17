



class CarsInSimulation:


    def __init__(self):
        '''dictionary of car id and departure time in seconds '''
        self.currentCarsAlive = {}
        self.numCarsDeparted = 0
        self.travelTimeCarsDeparted = 0

    def addCars(self,newCars, time):
        '''addCars(list of str, int) -> none'''
        for car in newCars:
            self.currentCarsAlive[car] = time

    def removeCars(self,removedCars, time):
        '''removeCars(list of str, int) -> none
        '''
        for car in removedCars:
            self.travelTimeCarsDeparted += time - self.currentCarsAlive[car]
        self.numCarsDeparted += len(removedCars)
