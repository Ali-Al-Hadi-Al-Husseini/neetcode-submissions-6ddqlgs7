class PrefixTree:

    def __init__(self):
        # or could and array of array by using ord chr
        self.trie = {}

    def insert(self, word: str) -> None:
        curr_node = self.trie

        for _char in word :
            if _char not in curr_node:
                curr_node[_char] = {}

            curr_node = curr_node[_char]

        curr_node[';']= {}

    def search(self, word: str) -> bool:
        curr_node = self.trie

        for _char in word :
            if _char not  in curr_node:
                return False

            curr_node = curr_node[_char]

        return ";" in curr_node

    def startsWith(self, prefix: str) -> bool:
            curr_node = self.trie

            for _char in prefix:
                if _char not in curr_node:
                    return False

                curr_node = curr_node[_char]

            return True     
        