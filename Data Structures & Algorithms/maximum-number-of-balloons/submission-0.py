class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_freq = Counter(text)
        ballo = Counter("balloon")

        return int(min([ char_freq[key] // ballo[key] for key in ballo.keys() ]))