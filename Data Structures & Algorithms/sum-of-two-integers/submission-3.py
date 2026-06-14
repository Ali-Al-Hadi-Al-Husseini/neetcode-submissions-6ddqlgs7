class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        res = 0
        carry = 0

        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            new_bit  = a_bit ^ b_bit ^ carry
            carry = (a_bit+ b_bit + carry) >= 2 

            if new_bit:
                res |= (1 << i)

        if res > 0x7FFFFFFF:
            res = ~(res ^ 0xFFFFFFFF )
        return res 