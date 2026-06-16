class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return f"{convret_to_int(num1) * convret_to_int(num2)}"

get_int={f"{i}":i for i in range(10)}

def convret_to_int(string):
    res = 0
    position = 1
    for i in range(len(string)-1,-1,-1):
        res += get_int[string[i]] * position
        position *= 10
    return res 
