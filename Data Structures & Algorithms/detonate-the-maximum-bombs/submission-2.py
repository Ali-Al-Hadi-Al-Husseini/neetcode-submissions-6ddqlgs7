from collections import defaultdict

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj_list = [[] for _ in range(len(bombs))]

        for i, (x,y,r) in enumerate(bombs):
            for j in range(i+1,len(bombs)):
                x1,y1,r1 = bombs[j]
                dist = ( ((x - x1) ** 2) + ((y - y1) ** 2)   ) ** 0.5

                if dist <= r1 :
                    adj_list[j].append(i)
                if dist <= r :
                    adj_list[i].append(j)
                    


        def dfs(curr_bomb, visited):
            if curr_bomb in visited:
                return 0

            visited.add(curr_bomb)
            bomb_count = 1

            for bomb in adj_list[curr_bomb]:
                bomb_count += dfs(bomb,visited)

            return bomb_count

        max_bombs = 0
        for bomb in range(len(bombs)):
            max_bombs = max(max_bombs,dfs(bomb,set()))

        return max_bombs 
