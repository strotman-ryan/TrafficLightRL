import traci


class EvaluatorStepListener(traci.StepListener):

      def __init__(self, evaluator):
            self.evaluator = evaluator
            
      def step(self, t=0):
            self.evaluator.evaluate()
            return True

      def print_results(self):
            self.evaluator.print_results()
