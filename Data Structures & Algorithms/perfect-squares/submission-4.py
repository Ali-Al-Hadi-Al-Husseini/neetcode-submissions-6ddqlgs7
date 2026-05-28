class Solution:
    def numSquares(self, n: int) -> int:
        memo= {0:0,1:1,2:2,3:3,4:1}
        
        def perfect_sqaure_numbers(num):
            if num <= 0 :
                return 0
            if num in memo:
                return memo[num]

            min_numbers = float("inf")
            for curr_square in range(get_closet_sqaure(num),0,-1):
                curr = perfect_sqaure_numbers(num - (curr_square**2))  +1
                min_numbers = min(min_numbers,curr)

            memo[num] = min_numbers
            return min_numbers

        return perfect_sqaure_numbers(n)



def get_closet_sqaure(num):
    curr = 1
    while  curr ** 2 <= num:
        curr  += 1
    return (curr - 1 )


