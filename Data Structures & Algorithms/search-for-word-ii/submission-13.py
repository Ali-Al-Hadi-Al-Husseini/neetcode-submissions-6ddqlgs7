class Trie:
    def __init__(self):
        self.childs = {}
        self.is_word = False
        self.word = ""

    def __contains__(self, key):
        return key in self.childs

    def __getitem__(self, key):
        return self.childs[key]

    def __setitem__(self, key, value):
        self.childs[key] = value

    def add_word(self, word):
        curr = self                  
        for ch in word:
            if ch not in curr:       
                curr[ch] = Trie()    
            curr = curr[ch]          
        curr.is_word = True
        curr.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        
        for word in words:
            trie.add_word(word)

        result = set()
        visiting = set()

        def dfs(row,col, trie):
            if (not ( -1 < row < len(board) )    or 
                not ( -1 < col < len(board[0])) or
                board[row][col] not in trie     or 
                (row,col) in visiting
                ):
                return
            trie = trie[board[row][col]]
            if trie.is_word:
                result.add(trie.word)
            
            visiting.add((row,col))

            dfs(row +1,col ,trie)
            dfs(row -1,col,trie)
            dfs(row,col +1,trie)
            dfs(row,col -1 ,trie)
            visiting.remove((row,col))

        
        for row in range(len(board)):
            for col in range(len(board[row])):
                dfs(row,col,trie)
        

        return list(result)

        
