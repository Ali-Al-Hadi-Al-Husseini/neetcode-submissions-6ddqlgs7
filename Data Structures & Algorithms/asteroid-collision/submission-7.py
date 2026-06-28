class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        collsion = asteroids[:]

        for idx, asteroid in enumerate(asteroids):
            if not stack or same_direction(asteroid,stack[-1][0]):
                if asteroid > 0:
                    stack.append((asteroid,idx))
                continue

            while stack and  not same_direction(asteroid,stack[-1][0]):
                prev_astroid,i = stack[-1]
                if abs(prev_astroid) > abs(asteroid):
      
                    collsion[idx] = None 
                    break
                elif abs(prev_astroid) < abs(asteroid):
                    collsion[i] = None
                    stack.pop() 
                else:
                    collsion[i]   = None 
                    collsion[idx] = None 
                    stack.pop() 
                    break
                
        res = []
        for asteroid in collsion:
            if not asteroid:
                continue
            res.append(asteroid)
        return res 
            



        

def same_direction(val1,val2):
    return (val1 <0 and val2 < 0) or( val1> 0 and val2 >0 )