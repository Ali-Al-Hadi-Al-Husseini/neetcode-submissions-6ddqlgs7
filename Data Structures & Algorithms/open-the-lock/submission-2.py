class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited_start = {}
        visited_target = {}

        deadends_set = set(deadends)
        queue = deque()
        queue.append(("0000",0,1)) # 1 for the start at 2 index
        queue.append((target,0,0)) # 0 for the end at 2 index

        while queue:
            curr = queue.popleft()
            
            if curr[0] in deadends_set:
                continue 
            if curr[0] in visited_start :
                if curr[2] == 0:
                    return curr[1] + visited_start[curr[0]]
                continue

            elif curr[0] in visited_target:
                if curr[2] == 1:
                    return curr[1] + visited_target[curr[0]]
                continue

            for child in get_children(curr):
                queue.append((child,curr[1] + 1 , curr[2]))

            if curr[2] == 1:
                visited_start[curr[0]] = curr[1]
            else:
                visited_target[curr[0]] = curr[1]

        return -1 
            


def get_children(curr):
    childs= []

    for i in range(4):
        childs.append(forward(curr[0],i))
        childs.append(backward(curr[0],i))

    return childs



def forward(curr,idx):
    new = list(curr)
    
    summ = int(new[idx]) + 1 
    new[idx] = str(summ % 10)
    return "".join(new)

def backward(curr,idx):
    new = list(curr)
    
    summ = int(new[idx]) - 1 
    new[idx] = str(summ % 10)
    return "".join(new)

        