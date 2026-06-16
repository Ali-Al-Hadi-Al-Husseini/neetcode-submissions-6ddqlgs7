class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return f"{convret_to_int(num1) * convret_to_int(num2)}"

def get_int(_chr):
    for i in range(10):
        if f"{i}" == _chr:
            return i

def convret_to_int(string):
    res = 0
    position = 1
    for i in range(len(string)-1,-1,-1):
        res += get_int(string[i]) * position
        position *= 10
    print(res)
    return res 
