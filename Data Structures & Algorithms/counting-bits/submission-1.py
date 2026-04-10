class Solution:
    def countBits(self, n: int) -> List[int]:
        memo = {}
        
        return [get_bits_count(i,memo) for i in range(n+1)]





def get_bits_count(n,memo):
    bits_count = 0

    while n >0:
        if n in memo:
            bits_count += memo[n]
            break
        if n & 1 == 1 :
            bits_count += 1

        n >>=1
    memo[n] = bits_count
    return bits_count
