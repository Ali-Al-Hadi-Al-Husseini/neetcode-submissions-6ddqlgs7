class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0,len(s) -1 
        notmatching = 0 # 1 
        meta ={"done": False, 'right':True,"l":0,"r":len(s)-1}
        
        while l < r :
            chr_rigth = s[l]
            chr_left = s[r]


            if s[l] == s[r]:
                l+= 1
                r -=1 
                continue

            if s[l] == s[r-1] and  not meta["done"] :
                meta["done"] = True
                meta["l"] = l
                meta["r"] = r
                r -= 1
                notmatching += 1



            elif s[r] == s[l+1] :
                if meta["done"] and meta["right"] :
                    l = meta['l']
                    r = meta['r']
                    meta["right"] = False
                    notmatching = 0 
                    continue
                l += 1
                notmatching += 1      

            else:
                if  meta["done"] and notmatching >= 1:
                    l = meta["l"]
                    r= meta["r"]
                    notmatching = 0
                    continue

                return False


        return notmatching < 2             