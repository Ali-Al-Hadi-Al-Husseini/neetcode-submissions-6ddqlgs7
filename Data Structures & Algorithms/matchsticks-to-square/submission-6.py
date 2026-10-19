class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        perimeter = sum(matchsticks) 
        if perimeter % 4 != 0 :
            return False

        expected_size = perimeter / 4
        sticks = {}
        

        for stick in matchsticks:
            if stick > expected_size:
                return False
            if stick not in sticks:
                sticks[stick] = 0
            sticks[stick] += 1 



        def helper(curr_size,sides):
            if sides == 4:
                return True
            
    
            for i in sticks.keys():
                if sticks[i] == 0 or curr_size + i > expected_size:
                    continue

                temp = curr_size + i
                sticks[i] -= 1


                if temp == expected_size and helper(0,sides + 1 ):
                    return True 
                elif helper(temp,sides):
                    return True 
                

                sticks[i] += 1  

            return False

        return helper(0,0)
