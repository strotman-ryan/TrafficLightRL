
from AbstractRLAgent import AbstractRLAgent
import random
import traci

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
        # add state if it is not already in dictionary
        if not (state in self._state_actions):
            print("new state encountered")
            self._state_actions[state] = [0 for x in range(num_actions)]

        current_time = traci.simulation.getTime()
        # choose next action e-greedy
        action = None
        if self._epsilon.GetResult(current_time) < random.random():
            # choose the max option
            print("chossing max")
            maximum = max(self._state_actions[state])
            possible_actions = [index for index, element in enumerate(self._state_actions[state]) if element == maximum]
            print("possible actions are: " + str(possible_actions))
            action = random.choice(possible_actions)
        else:
            print("choosing random")
            action = random.randint(0, num_actions - 1)
        print("choosing max: action " + str(action))

        print("time: " + str(current_time))
        '''see if state is valid, if phase at 1,3(yellow lights) not valid'''
        if self.lastState:
            self._state_actions[self.lastState][self.lastAction] += self._alpha.GetResult(current_time) * (
                    reward + self._discount * max(self._state_actions[state]) - self._state_actions[self.lastState][
                self.lastAction])

        self.lastAction = action
        self.lastState = state
        return action
