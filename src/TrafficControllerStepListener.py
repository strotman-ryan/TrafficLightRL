
import traci
import traci.constants as tc
import random

class TrafficControllerStepListener(traci.StepListener):

    def __init__(self):
        '''state is key (phase,[waiting in lanes])->[stay expected reward, change expected reward]'''
        self.stateActions = {}
        self.pastState = None
        self.pastAction = None
        self.junction = "C"
        self.tl = "gneJ1"
        self.lanes = ["EC_0","NC_0","WC_0","SC_0"]
        traci.junction.subscribeContext("C",tc.CMD_GET_VEHICLE_VARIABLE,40,[tc.VAR_SPEED,tc.VAR_LANE_ID])
        self.lastState = None
        self.lastAction = None
        self.alpha = .05
        self.discount = .9
        self.epsilon = .1
        self.counter = 0
        random.seed(0)
        
    def step(self,t=0):
        #get state
        if self.counter % 3 == 0:
            reward, state = self.getStateAndReward()
            print((reward, state))
            self.makeAction(reward,state)
        self.counter += 1
        return True
        
    def getStateAndReward(self):
        '''getState()->(phase int, [cars waitng for each lane])'''
        vehicles = traci.junction.getContextSubscriptionResults(self.junction)
        tlPhase = traci.trafficlight.getPhase(self.tl)
        if not vehicles:
            return 0,(tlPhase,) +tuple([0 for x in self.lanes])
        reward = 0
        state = [0 for x in self.lanes]
        for vehicle in vehicles.values():
            if vehicle[tc.VAR_SPEED] <= 11.176 and vehicle[tc.VAR_LANE_ID] in self.lanes:
                 #find number of vechicles that have speed less than .1m/s in incomming lanes
                reward -= 1
                state[self.lanes.index(vehicle[tc.VAR_LANE_ID])] += 1
        state = [min(lane,11)/2 for lane in state]
        return reward, (tlPhase,) + tuple(state)

    def makeAction(self,reward, state):
        #add state if it is not already in list
        if not(state in self.stateActions):
            self.stateActions[state] = [0,0]
        
        '''see if state is valid, if phase at 1,3(yellow lights) not valid'''
        if self.lastState:
            '''last state was not valid so update the first action'''
            self.stateActions[self.lastState][self.lastAction] += self.alpha * (reward + self.discount * max(self.stateActions[state]) - self.stateActions[self.lastState][self.lastAction])
            
        valid = state[0] in [0,2]
        action = None
        if valid:
            '''update past state action'''
            #choose next action e-greedy
            if self.epsilon < random.random():
                #choose the max option
                action = self.stateActions[state].index(max(self.stateActions[state]))
            else:
                action = random.randint(0,len(self.stateActions[state]) -1)
            if action == 0:
                '''stay at phase'''
                traci.trafficlight.setPhase(self.tl,state[0])
            elif action == 1:
                '''go to next phase'''
                traci.trafficlight.setPhase(self.tl,state[0] + 1)
        else:
            #dummy so can update other values
            action = 0
        print(action)
        self.lastAction = action
        self.lastState = state
        return
