
from AbstractRLAgent import AbstractRLAgent
import random

class RLAgentQLearning(AbstractRLAgent):

    def __init__(self, epsilon, alpha, discount):
        self._epsilon = epsilon
        self._alpha = alpha
        self._discount = discount
        self._state_actions = {}
        self.lastState = None
        self.lastAction = None
        random.seed(0)

    def get_action(self, state, reward, num_actions):
        # add state if it is not already in list
        if not (state in self._state_actions):
            self._state_actions[state] = [0 for x in range(num_actions)]

        '''see if state is valid, if phase at 1,3(yellow lights) not valid'''
        if self.lastState:
            self._state_actions[self.lastState][self.lastAction] += self._alpha * (
                    reward + self._discount * max(self._state_actions[state]) - self._state_actions[self.lastState][
                self.lastAction])

        action = None
        # choose next action e-greedy
        if self._epsilon < random.random():
            # choose the max option
            action = self._state_actions[state].index(max(self._state_actions[state]))
        else:
            action = random.randint(0, num_actions - 1)
        self.lastAction = action
        self.lastState = state
        return action