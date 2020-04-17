#title: runner.py
#Author: Ryan Strotman
#synopsis:make a simulation run



#get ready for TraCl
import os, sys
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

from sumolib import checkBinary
import traci
from CarsInSimulation import CarsInSimulation
import traci.constants as tc
from EvaluatorStepListener import EvaluatorStepListener
from TrafficControllerStepListener import TrafficControllerStepListener

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
    evaluator = EvaluatorStepListener(CarsInSimulation())
    controller = TrafficControllerStepListener()
    traci.addStepListener(evaluator)
    traci.addStepListener(controller)
    runSimulation()
    evaluator.PrintResults()
    print(controller.stateActions)
