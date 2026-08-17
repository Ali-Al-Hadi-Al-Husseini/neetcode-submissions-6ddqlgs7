class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        paths = path.split("/")

        for dir_name in paths:
            if dir_name == "..":
                if res:
                    res.pop()
            elif dir_name  and dir_name!= ".":
                res.append(dir_name)
        
        return "/" + "/".join(res)