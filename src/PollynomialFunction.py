

from AbstractFunction import AbstractFunction
import math

class PollynomialFunction(AbstractFunction):

      def __init__(self, exponent):
      	  self._exponent_value= exponent

      def GetResult(self, time):
            print("result is: " + str(math.pow(time,self._exponent_value)))
            return math.pow(time, self._exponent_value)
