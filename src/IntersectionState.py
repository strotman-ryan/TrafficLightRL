
import traci
import traci.constants as tc

class IntersectionState:

    def __init__(self, intersection_id):
        self.intersection_id = intersection_id
        self.tl = "gneJ1"
        self.lanes = ["EC_0", "NC_0", "WC_0", "SC_0"]
        traci.junction.subscribeContext(self.intersection_id, tc.CMD_GET_VEHICLE_VARIABLE, 40, [tc.VAR_SPEED, tc.VAR_LANE_ID])

    def get_state_and_reward(self):
        """getState()->(phase int, [cars waitng for each lane])"""
        vehicles = traci.junction.getContextSubscriptionResults(self.intersection_id)
        tlPhase = traci.trafficlight.getPhase(self.tl)
        if not vehicles:
            return 0, (tlPhase,) + tuple([0 for x in self.lanes])
        reward = 0
        state = [0 for x in self.lanes]
        for vehicle in vehicles.values():
            if vehicle[tc.VAR_SPEED] <= 11.176 and vehicle[tc.VAR_LANE_ID] in self.lanes:
                # find number of vehicles that have speed less than .1m/s in incomming lanes
                reward -= 1
                state[self.lanes.index(vehicle[tc.VAR_LANE_ID])] += 1
        state = [min(lane, 11) / 2 for lane in state]
        return reward, (tlPhase,) + tuple(state)