class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def dfs(row,col,idx):
            if row < 0 or row >= len(board) or col <0 or col >= len(board[0]):
                return False
            if idx >= len(word) or board[row][col] != word[idx] :
                return False
            if (row,col) in visited:
                return False
            if idx == len(word) - 1 and word[idx] == board[row][col]:
                return True

            
            visited.add((row,col))
            idx +=1 
            found = (
            dfs(row+1,col,idx) or
            dfs(row,col +1,idx) or
            dfs(row -1,col,idx) or
            dfs(row,col -1,idx))
            visited.remove((row,col))
            return found    

        found = False
        for row in range(len(board)):
            for col in range(len(board[row])):
                visited = set()
                found |= dfs(row,col,0)
                if found: return True

        return found
    
board=[["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word="ABCESEEEFS"
sol = Solution().exist(board, word)
print(sol)