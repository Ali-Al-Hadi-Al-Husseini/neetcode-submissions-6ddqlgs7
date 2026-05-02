class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        curr_trie = self.trie

        for _chr in word:
            if _chr not in curr_trie:
                curr_trie[_chr] = {}
            curr_trie = curr_trie[_chr]
        curr_trie["@"] = {}
        

    def search(self, word: str) -> bool:
        curr_trie = self.trie
        idx = 0
        while idx < len(word):
            _chr = word[idx]
            if _chr not in curr_trie and _chr != ".":
                return False
            if _chr == ".":
                has_chr,skipped ,curr_trie = handle_dot(word[idx:],curr_trie)
                idx += skipped
                if not has_chr:
                    return False
            else:
                curr_trie = curr_trie[_chr]
                idx += 1

        return "@" in curr_trie



def handle_dot(word, trie):
    idx = 0
    while idx < len(word) and word[idx] == ".":
        idx += 1
    depth = idx +1

    if idx >= len(word):
        has_the_depth,new_trie = has_depth(idx, trie)
        return has_the_depth, idx,new_trie

    has_chr, new_trie = dfs(word[idx],depth,trie,True)
    return has_chr, idx, new_trie


def has_depth(depth, Trie):
    if depth == 0 :
        return "@" in Trie, Trie

    for trie in Trie.values():
        has_needed_depth, new_Trie = has_depth(depth - 1, trie)
        if has_needed_depth:
            return True, new_Trie
        
    return False, Trie


def dfs(_chr,depth,Trie, is_first = False):
    if depth == 0 :
        return False,None
    if _chr in Trie and not is_first:
        return True,Trie


    for trie in Trie.values():
        has_chr, new_trie = dfs(_chr,depth-1,trie)
        if has_chr:
            return has_chr, new_trie

    return False, None








