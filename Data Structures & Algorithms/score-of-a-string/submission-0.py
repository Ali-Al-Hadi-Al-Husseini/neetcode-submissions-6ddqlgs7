class Solution:
    def scoreOfString(self, s: str) -> int:
        asci_sum = 0

        for i in range(1,len(s)):
            asci_sum += abs(ord(s[i])- ord(s[i-1]))

        return asci_sum
             