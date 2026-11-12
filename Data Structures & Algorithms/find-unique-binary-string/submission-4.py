class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        bin_set = set(nums)
        n = len(nums)

        for i in range(n +1 ):
            bin_str =  make_bin(i,n) 
            if bin_str not in bin_set:
                return bin_str
        
        return "1"  * n



def make_bin(num,n):
    num = str(bin(num))[2:]
    return ("0" * (n - len(num) )) + num 