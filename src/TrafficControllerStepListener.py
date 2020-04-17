import traci
import traci.constants as tc
import random


class TrafficControllerStepListener(traci.StepListener):
    def __init__(self, controller):
        self.controller = controller
        self.junction = "C"



    def step(self, t=0):
        self.controller.control_lights()
        return True




