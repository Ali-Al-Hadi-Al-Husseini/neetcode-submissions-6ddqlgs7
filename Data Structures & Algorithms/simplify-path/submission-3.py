class Solution:
    def simplifyPath(self, path: str) -> str:
        dir_chars = set(list("qwertyuiopsdfgahjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890_."))
        res = []
        idx = 0
        

        while idx < len(path):
            
            while idx < len(path) and  path[idx] == "/":
                idx += 1 
            
            curr_dir = ""
            dots = 0 
            start_idx = idx 
            while idx < len(path) and path[idx] in dir_chars :
                if path[idx] == ".":
                    dots += 1 
                curr_dir += path[idx]
                idx += 1 

            if  idx - start_idx  == 2 == dots :
                curr_dir = ""
                if res:
                    res.pop()
                
            if curr_dir and curr_dir != ".":
                res.append(curr_dir)

            print(res)

        return  "/"+ "/".join(res)