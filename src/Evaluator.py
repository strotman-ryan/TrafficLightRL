import traci


class Evaluator:

    def __init__(self):
        """dictionary of car id and departure time in seconds """
        self.currentCarsAlive = {}
        self.numCarsDeparted = 0
        self.travelTimeCarsDeparted = 0

    def evaluate(self):
        current_time = traci.simulation.getTime()
        self._remove_cars(traci.simulation.getArrivedIDList(), current_time)
        self._add_cars(traci.simulation.getDepartedIDList(), current_time)

    def print_results(self):
        print("total cars: " + str(self.numCarsDeparted))
        print("total travel time: " + str(self.travelTimeCarsDeparted))
        print("average travel time: " + str(self.travelTimeCarsDeparted / self.numCarsDeparted))

    def _add_cars(self, new_cars, time):
        """addCars(list of str, int) -> none"""
        for car in new_cars:
            self.currentCarsAlive[car] = time

    def _remove_cars(self, removed_cars, time):
        """removeCars(list of str, int) -> none"""
        for car in removed_cars:
            self.travelTimeCarsDeparted += time - self.currentCarsAlive[car]
        self.numCarsDeparted += len(removed_cars)
