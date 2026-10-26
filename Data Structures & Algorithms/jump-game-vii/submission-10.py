class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        queue = deque()
        queue.append(0)
        visiting = set()


        while queue :
            curr_node = queue.popleft()
            if curr_node == len(s) -1 :
                return True
            start = min(curr_node+maxJump,len(s)-1)
            end = curr_node +minJump -1 
            for node in range(start, end ,-1  ):
                if s[node] == "0" and not node in visiting:
                    queue.append(node)
                    visiting.add(node)

        return False 