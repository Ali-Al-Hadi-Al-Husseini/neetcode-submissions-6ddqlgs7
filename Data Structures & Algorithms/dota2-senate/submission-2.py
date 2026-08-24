class Solution:
    def predictPartyVictory(self, senates: str) -> str:
        d = 0
        r = 0
        senate = list(senates)
        for sen in senate:
            if sen == "R":
                r += 1
            else:
                d += 1
            
        print("count",d,r)
        r_blocked = 0
        d_blocked = 0 

        i = 0 

        while 1 < len(senate):
            if senate[i] == "R":
                if r_blocked > 0 :
                    r_blocked -= 1 
                    senate.pop(i)

                else:
                    d_blocked += 1 
                    d -= 1 
                    if d <= 0:
                        return "Radiant"
                    i += 1
            else:
                if d_blocked > 0 :
                    d_blocked -= 1 
                    senate.pop(i)
                else:
                    r_blocked += 1 
                    r -= 1 
                    if r <= 0:
                        return "Dire"
                    i +=1 
                    
            if i >= len(senate):
                i = 0 

        return "Radiant" if senate[0] == "R" else "Dire"