class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5:0,10:0,20:0}

        for bill in bills:
            change[bill] += 1
            
            change_needed = bill - 5 
            if change_needed == 0: continue


            while change_needed > 10 :
                if change[10] <= 0 :
                    break
                change[10] -= 1 
                change_needed -= 10
            
            while change_needed >= 5  :
                if change[5] <= 0 :
                    return False
                change[5] -= 1 
                change_needed -= 5              
            
        return True 



        