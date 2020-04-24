
from AbstractTLController import AbstractTLController
import traci


class RlTlController(AbstractTLController):

    def __init__(self, state_retriever, agent):
        self.state_retriever = state_retriever
        self.agent = agent
        self.tl = "C"


    def control_lights(self):
        print("-----------new step -----------------")
        reward, state = self.state_retriever.get_state_and_reward()
        action = self.agent.get_action(state, reward, 2)
        print("state: " + str(state))
        print("Reward: " + str(reward))
        print("action #: " + str(action))
        if state[0] in [1,3]:
            print("no choice")
            return
        if action == 1:
            '''stay at phase'''
            print("staying at phase")
            traci.trafficlight.setPhase(self.tl, state[0])
        if action == 0:
            '''go to next phase'''
            print("next phase")
            traci.trafficlight.setPhase(self.tl, (state[0] + 1) % 4)
