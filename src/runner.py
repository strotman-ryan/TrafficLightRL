#title: runner.py
#Author: Ryan Strotman
#synopsis:make a simulation run

#comment from pycharm

#get ready for TraCl
import os, sys
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

from sumolib import checkBinary
import traci
from Evaluator import Evaluator
import traci.constants as tc
from EvaluatorStepListener import EvaluatorStepListener
from TrafficControllerStepListener import TrafficControllerStepListener
from RlTlController import RlTlController
from IntersectionState import IntersectionState
from RLAgentQLearning import RLAgentQLearning

def runSimulation():
    '''runSimulation(CarsInSimulation) -> none'''
    while traci.simulation.getMinExpectedNumber()>0:
        traci.simulationStep()
    traci.close()


def setUpSimulation():
    sumoBinary = checkBinary("sumo-gui")
    sumoCmd = [sumoBinary, "-c", "data/first.sumocfg"]
    traci.start(sumoCmd)
    


if __name__ == "__main__":
    setUpSimulation()
    sl_evaluator = EvaluatorStepListener(Evaluator())
    q_learning = RLAgentQLearning(.05, .2, .9)
    state = IntersectionState("C")
    controller = RlTlController(state, q_learning)
    sl_controller = TrafficControllerStepListener(controller)
    traci.addStepListener(sl_evaluator)
    traci.addStepListener(sl_controller)
    runSimulation()
    sl_evaluator.print_results()
