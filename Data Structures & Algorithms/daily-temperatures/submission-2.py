class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack = []
        result = [0 for _ in temperatures]

        for idx,temp in enumerate(temperatures):
            while temp_stack and temperatures[temp_stack[-1]] < temp:
                i= temp_stack.pop()  
                result[i] = idx - i 

            temp_stack.append(idx)

        return result

