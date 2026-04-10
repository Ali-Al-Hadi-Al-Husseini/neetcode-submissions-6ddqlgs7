class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {_char:idx for idx, _char in enumerate(order)}
        last_word = words[0]

        for word in words:
            if not inorder(last_word,word,order_dict):
                return False

            last_word = word

        return True


def inorder(word1,word2,order):
    if word1 == word2:return True 

    for idx in range(len(word1)):
        if idx >= len(word2):
            return False
        if order[word1[idx]] == order[word2[idx]]:
            continue
        elif order[word1[idx]] < order[word2[idx]]:
            return True
        elif order[word1[idx]] > order[word2[idx]]:
            return False

    return True 