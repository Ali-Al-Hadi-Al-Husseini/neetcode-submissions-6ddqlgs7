class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack = []
        result = [0 for _ in temperatures]

        for idx,temp in enumerate(temperatures):


            while len(temp_stack) > 0 and temp_stack[-1][0] < temp:
                tmp,i= temp_stack.pop()  
                result[i] = idx - i 

            temp_stack.append((temp,idx))

        return result

