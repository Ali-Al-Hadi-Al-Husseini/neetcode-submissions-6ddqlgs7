class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        place = 31 

        while n :
            last_bit = n & 1 
            n >>= 1 
            result += last_bit * (2 ** place )
            place -= 1 

        return result 