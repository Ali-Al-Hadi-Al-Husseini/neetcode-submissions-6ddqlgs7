class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        ops_set = {"+","C","D"}

        for ops in operations:
            if ops in ops_set:
                if ops == "+":
                    new_num = stack[-1] + stack[-2]
                    stack.append(new_num)
                elif ops == "C":
                    stack.pop()
                else:
                    new_num = stack[-1] + stack[-1]
                    stack.append(new_num)
                continue
            stack.append(int(ops))


        return sum(stack)