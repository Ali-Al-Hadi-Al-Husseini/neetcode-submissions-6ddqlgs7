class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        left,right = 0,len(gas) - 1
        gas_tank = gas[right]- cost[right]

        while right > left:
            if gas_tank < 0 :
                right -= 1 
                gas_tank += gas[right]- cost[right]
            else:
                gas_tank += gas[left] - cost[left]
                left += 1


        return right if gas_tank >= 0 else -1