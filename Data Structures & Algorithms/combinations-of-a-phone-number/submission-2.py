class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_map = {
                '2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'], 
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r','s'],
                '8': ['v', 't', 'u'],
                '9': ['y', 'w', 'x','z']}

        result  = []
        curr_comb = []
        def get_combination(idx):
            if idx >= len(digits):
                result.append("".join(curr_comb))
                return

            for _chr in num_map[digits[idx]]:
                curr_comb.append(_chr)
                get_combination(idx+1)
                curr_comb.pop()

        get_combination(0)
        return result if result !=[""] else []

            




def leters(i):
    start = (i - 1) * 3
    end = i * 3 
    return [chr(ord("a") + idx) for idx in range(start,end)]
    