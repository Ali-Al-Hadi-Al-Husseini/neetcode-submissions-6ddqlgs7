class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = set(['+', '-', '*','/'])
        stack = []

        for tok in tokens:
            if tok not in operations:
                stack.append(tok)
                continue
            val2 = stack.pop()
            val1 = stack.pop()
            stack.append(calculate(val1,val2,tok))            

        return int(stack[-1])




def calculate(val1, val2, operation):

    if operation == "+":
        return int(val1) + int(val2)
    if operation == "-":
        return int(val1) - int(val2)    
    if operation == "*":
        return int(val1) * int(val2)    
    if operation == "/":
        return int(val1) / int(val2)