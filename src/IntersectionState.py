
import traci
import traci.constants as tc
import math
class IntersectionState:

    def __init__(self, intersection_id):
        self.intersection_id = intersection_id
        self.tl = "C"
        self.lanes = ["EC_0", "NC_0", "WC_0", "SC_0"]
        traci.junction.subscribeContext(self.intersection_id, tc.CMD_GET_VEHICLE_VARIABLE,150, [tc.VAR_SPEED, tc.VAR_LANE_ID])

    def get_state_and_reward(self):
        """getState()->(phase int, [cars waitng for each lane])"""
        vehicles = traci.junction.getContextSubscriptionResults(self.intersection_id)
        tl_phase = traci.trafficlight.getPhase(self.tl)
        if not vehicles:
            return 0, (tl_phase,) + tuple([0 for x in self.lanes])
        reward = 0
        state = [0 for x in self.lanes]
        for vehicle in vehicles.values():
            if vehicle[tc.VAR_SPEED] <= .1:
                reward -= 1
            if  vehicle[tc.VAR_LANE_ID] in self.lanes:
                state[self.lanes.index(vehicle[tc.VAR_LANE_ID])] += 1
        #state = [int(math.log(lane+1,2)) for lane in state]  # turn this into a log
        #state = [min(1, lane) for lane in state]
        return reward, (tl_phase,) + tuple(state)
