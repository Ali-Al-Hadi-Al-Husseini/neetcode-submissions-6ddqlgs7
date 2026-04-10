class Solution:
    def isHappy(self, n: int) -> bool:
        slow  = calc(n)
        fast = calc(slow)


        while fast != 1 and fast != slow :
            slow = calc(slow)
            fast = calc(calc(fast))

        return fast == 1 or slow == 1 










def calc (number):
    res = 0
    for digit in str(number):
        digit = int(digit)
        res += digit * digit

    return res 