
from AbstractTLController import AbstractTLController
import traci


class RlTlController(AbstractTLController):

    def __init__(self, state_retriever, agent):
        self.state_retriever = state_retriever
        self.agent = agent
        self.tl = "gneJ1"


    def control_lights(self):
        reward, state = self.state_retriever.get_state_and_reward()
        action = self.agent.get_action(state, reward, 2)
        # TODO: this will cause accidents rn
        if action == 0:
            '''stay at phase'''
            traci.trafficlight.setPhase(self.tl, state[0])
        if action == 1:
            '''go to next phase'''
            traci.trafficlight.setPhase(self.tl, (state[0] + 1) % 4)
