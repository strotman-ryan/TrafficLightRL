

from AbstractFunction import AbstractFunction

class ConstantFunction(AbstractFunction):

    def __init__(self, value):
        self._constant_value = value



    def GetResult(self, time):
        return self._constant_value
