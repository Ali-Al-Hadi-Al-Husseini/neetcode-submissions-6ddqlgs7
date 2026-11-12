class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        bin_set = set(nums)
        n = len(nums)


        for i in range(n +1 ):
            if make_bin(i,n) not in bin_set:
                return make_bin(i,n)
        
        return "1"  * n



def make_bin(num,n):
    num = str(bin(num))[2:]
    return ("0" * (n - len(num) )) + num 