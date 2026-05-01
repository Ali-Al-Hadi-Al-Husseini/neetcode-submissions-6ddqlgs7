class Solution:
    def myPow(self, x: float, n: int) -> float:
        power = abs(n)
        result = 1
        current_product = x
        
        while power > 0:
            if power % 2 == 1:
                result *= current_product
            
            current_product *= current_product
            power //= 2
            
        return result if n >= 0 else 1 / result