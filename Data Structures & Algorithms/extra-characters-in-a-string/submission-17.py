class Trie:
    def __init__(self,s):
        self.node = {}
        self.s  = s 

    def add_word(self,word):
        curr_node = self.node
        
        for _chr in word:
            if _chr not in curr_node:
                curr_node[_chr] = {}
            curr_node = curr_node[_chr] 

        curr_node["*"] = True

    def find(self,idx):
        s = self.s
        words= []
        curr_node = self.node

        while idx < len(s) and s[idx] in curr_node:
            curr_node =curr_node[s[idx]]
            idx += 1 
            if "*" in curr_node:
                words.append(idx)

        return words
        

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie(s)
        for word in dictionary:
            trie.add_word(word)

        memo = {len(s):0}
        def helper(idx):
            old_idx = idx 
            if idx in memo:
                return memo[idx]

            
            min_res = 1 + helper(idx + 1 )
            for word in trie.find(idx) :
                min_res = min(min_res,helper(word))


            memo[old_idx] = min_res 
            return memo[old_idx]
        
        return helper(0)