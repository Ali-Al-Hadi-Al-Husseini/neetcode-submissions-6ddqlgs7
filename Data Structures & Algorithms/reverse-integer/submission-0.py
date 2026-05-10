class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        res = int(str(abs(x))[::-1]) * sign
        low, high = -2**31, 2**31 - 1
        
        return res if low <= res <= high else 0