class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False 


        return helper(s1,s2,s3)or helper(s2,s1,s3)



def helper(s1,s2,s3):
    n, m = 0,0
    i,j,k = 0,0,0


    while k < len(s3):
        curr_n , curr_m = 0, 0 
        start_k = k

        while i < len(s1) and s1[i] == s3[k] :
            curr_n += 1 
            i += 1 
            k += 1 
        if curr_n != 0:
            n +=1 

        while j < len(s2) and s2[j] == s3[k]:
            curr_m += 1 
            j += 1
            k += 1 
            
        if curr_m != 0:
            m +=1 
        if k == start_k:
            return False
                

    return True 