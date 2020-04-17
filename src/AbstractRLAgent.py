
from abc import ABC, abstractmethod


class AbstractRLAgent(ABC):

    @abstractmethod
    def get_action(self, state, reward, num_actions):
        """get_action(tuple,int, int) -> int in [0,num_actions-1]"""
        pass
