class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        curr_num = calc(n)

        while curr_num != 1 and not (curr_num in visited):
            visited.add(curr_num)
            curr_num = calc(curr_num)

        return curr_num == 1










def calc (number):
    res = 0
    for digit in str(number):
        digit = int(digit)
        res += digit * digit

    return res 