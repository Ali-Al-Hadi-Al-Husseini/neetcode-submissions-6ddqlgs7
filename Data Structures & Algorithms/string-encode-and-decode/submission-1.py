class Solution:

    def encode(self, strs: List[str]) -> str:
        print(strs)
        return "".join([f"#{len(word)}#{word}" for word in strs])
        
    def decode(self, s: str) -> List[str]:
        res = []
        idx = 0 

        while idx < len(s):
            if s[idx] == "#":
                idx+=1 
                length = []

                while s[idx] != "#":
                    length.append(s[idx])
                    idx += 1 

                length = int("".join(length))
                
                res.append(s[idx+1:idx+length+1])
                idx += length 
            idx += 1 
        return res 
                
