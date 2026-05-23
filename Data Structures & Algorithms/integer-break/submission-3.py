class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {(2,1):1,(3,1):2}

        def get_max_product(n,curr_product):
            if n == 0 :
                return curr_product
            if (n,curr_product) in memo:
                return memo[(n,curr_product)]

            curr_max_product = curr_product
            for integer in range(1,n+1):
                if n - integer < 0 : continue
                
                new_product = get_max_product(n - integer,curr_product * integer)
                curr_max_product = max(curr_max_product,new_product)

            memo[(n,curr_product)] = curr_max_product
            return curr_max_product

        return get_max_product(n,1)
    