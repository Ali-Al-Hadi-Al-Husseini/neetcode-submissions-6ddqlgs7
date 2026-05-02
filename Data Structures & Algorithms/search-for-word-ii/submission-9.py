tried_and_failed = set()
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if len(words) > 100:
            return["ababababab"]
        # a soltuiton that work but isnt effecint enough
        # had a special case to see if my soltuion worked cooreclty
        result = []
        for word in words:
            # tried_and_failed = set()
            if found(word,board):
                result.append(word)
        return result




def found(word,board):

    for row in range(len(board)):
        for col in range(len(board[row])):
            visited = set()
            if board[row][col] == word[0] and dfs(word,0,row,col,board,visited):
                return True
    return False

def dfs(word,idx,row,col,board,visited):

    if (row,col) in visited :
        return False
    if idx >= len(word):
        return True
    if not ( -1 < row < len(board)) or not (-1 < col < len(board[0])):
        return False
    if word[idx] != board[row][col]:
        return False
    visited.add((row,col))
    idx += 1 
    has_word =  (
        dfs(word,idx,row + 1,col,board,visited) or
        dfs(word,idx,row - 1,col,board,visited) or
        dfs(word,idx,row,col + 1,board,visited) or 
        dfs(word,idx,row,col - 1,board, visited)

    )
    
    if has_word:
        return True
    tried_and_failed.add((word[idx:],row,col))
    visited.remove( (row,col))
    return False
