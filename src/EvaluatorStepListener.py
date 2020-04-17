
import traci

class EvaluatorStepListener(traci.StepListener):
      
      
      def __init__(self, cars):
      	    self.cars = cars
            
      def step(self, t=0):
            currentTime = traci.simulation.getTime();	
	    self.cars.removeCars(traci.simulation.getArrivedIDList(),currentTime)
            self.cars.addCars(traci.simulation.getDepartedIDList(), currentTime)
            return True

      def PrintResults(self):
             print("total cars: " + str(self.cars.numCarsDeparted))
             print("total travel time: " + str(self.cars.travelTimeCarsDeparted))
             print("average travel time: " + str(self.cars.travelTimeCarsDeparted/self.cars.numCarsDeparted))
