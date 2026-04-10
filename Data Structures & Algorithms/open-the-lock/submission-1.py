class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead_ends = set(deadends)
        visited = set()
        queue = [("0000",0)]
        
        

        while queue:
            curr,curr_len = queue.pop(0) # pop(0) big O is O(n) i could use linkedlist or q built in data type 

            if curr in dead_ends or curr in visited:
                continue

            for i in range(4):
                new = (forward(curr,i),curr_len +1)
                if new[0] == target:
                    return new[1]
                queue.append(new)
                new = (backward(curr,i),curr_len +1)
                if new[0] == target:
                    return new[1]
                queue.append(new)


            visited.add(curr)

        return -1 



def forward(curr,idx):
    new = list(curr)
    
    summ = int(new[idx]) + 1 
    new[idx] = str( summ % 10 )
    return "".join(new)

def backward(curr,idx):
    new = list(curr)
    
    summ = int(new[idx]) - 1 
    new[idx] = str(summ % 10)
    return "".join(new)
