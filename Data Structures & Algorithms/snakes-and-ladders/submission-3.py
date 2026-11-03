class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        distance = [float("inf")] * ( 1+ n * n)
        distance[1] = 0 

        rolls = 1
        passed = 0
        loop_back = 0

        for r in range(n-1,-1,-1):
            should_rev = n % 2 == r % 2
            for c in  range(n-1,-1,-1) if should_rev else range(n):
                if (r,c) == (n-1,0): continue
                idx = get_idx(r,c,n)
                
                if board[r][c] != -1:
                    distance[board[r][c]] = min(distance[idx]+1,rolls,distance[board[r][c]] )
                    if board[r][c] <= (idx - passed):
                        loop_back += 1 


                if loop_back == 6:
                    break
                if distance[idx] < rolls:
                    rolls = distance[idx] +1
                    passed = 0
                    loop_back = 0
                    continue
                    
                distance[idx] = min(distance[idx],rolls)
                passed += 1 
                if passed == 6:
                    rolls += 1 
                    passed = 0 
                    loop_back = 0 


        return distance[-1] if distance[-1] != float("inf") else -1 





def get_idx(r,c,n):
    if r % 2 == n % 2 :
        c = -(c - (n-1))
    r = -(r - (n-1))
    r *= n
    return r + c +1 

