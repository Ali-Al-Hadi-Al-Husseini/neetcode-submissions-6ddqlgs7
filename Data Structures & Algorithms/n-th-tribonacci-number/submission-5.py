class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 0 : return 0 
        if n == 1: return 1
        if n == 2: return 1

        curr_fib = 0
        t1, t2, t3 = 0,1,1

        for _ in range(n-2):
            curr_fib = t1 + t2 +t3
            t1 = t2
            t2 = t3
            t3 = curr_fib 

        return curr_fib