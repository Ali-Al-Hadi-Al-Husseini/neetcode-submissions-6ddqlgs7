class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        queue = deque()
        queue.append(0)
        farthest = 0


        while queue :
            curr_node = queue.popleft()

            start = max(curr_node  + minJump,farthest +1 )
            end =  min(curr_node+maxJump +1 ,len(s))
            for node in range(start, end ):
                if s[node] == "0":
                    if node == len(s) -1 :
                        return True
                    queue.append(node)

            farthest = curr_node + maxJump

        return False 