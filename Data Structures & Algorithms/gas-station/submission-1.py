class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
            if sum(cost) > sum(gas):
                return -1

            gas_tank = 0
            res = 0
            for idx in range(len(gas)):
                gas_tank += gas[idx]
                gas_tank -= cost[idx]

                if gas_tank < 0:
                    gas_tank = 0
                    res = idx +1

            return res 