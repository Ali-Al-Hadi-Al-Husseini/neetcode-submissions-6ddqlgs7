class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute Force 
        temp_stack = []

        for idx,temp in enumerate(temperatures):
            days = 0 
            for curr_temp in temperatures[idx:]:
                if curr_temp > temp:
                    temp_stack.append(days)
                    break
                days += 1 
                
            if days == len(temperatures) - idx :
                temp_stack.append(0)

        return temp_stack