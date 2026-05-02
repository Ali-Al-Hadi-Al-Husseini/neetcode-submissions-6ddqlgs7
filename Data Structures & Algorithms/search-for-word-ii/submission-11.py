tried_and_failed = set()
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = []
        grid_letters = set()

        for row in range(len(board)):
            for col in range(len(board[0])):
                grid_letters.add(board[row][col])

        for word in words:
            # tried_and_failed = set()
            if has_letter(word,grid_letters) and found(word,board):
                result.append(word)
        return result


def has_letter(word,grid_letters) :

    for _chr in word:
        if _chr not in grid_letters:
            return False
    return True

def found(word,board):

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == word[0] and dfs(word,0,row,col,board):
                return True
    return False

def dfs(word,idx,row,col,board,):
    if idx >= len(word):
        return True
    if not ( -1 < row < len(board)) or not (-1 < col < len(board[0])):
        return False
    if word[idx] != board[row][col]:
        return False
    board[row][col] = "@"
    idx += 1 
    has_word =  (
        dfs(word,idx,row + 1,col,board) or
        dfs(word,idx,row - 1,col,board) or
        dfs(word,idx,row,col + 1,board) or 
        dfs(word,idx,row,col - 1,board)

    )
    board[row][col] = word[idx-1]
    if has_word:
        return True

    return False
