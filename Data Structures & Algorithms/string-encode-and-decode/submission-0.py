class Solution:
    
    def encode(self, strs: List[str]) -> str:
        result = []
        for idx, word in enumerate(strs):
            delimeter = delimeter_maker(len(word))
            result.append(delimeter)
            result.append(word)
        
        return "".join(result)


    def decode(self, s: str) -> List[str]:
        idx = 0
        result = []
        while idx < len(s):
            if s[idx] == "#":
                j = idx + 1 
                while j< len(s) and s[j] != "#":
                    j += 1 

                valid, length = is_delimeter(s[idx:j+1])
                if valid :
                    idx = j + 1
                    decoded_string = s[idx:idx+length]
                    result.append(decoded_string)
                    continue 
            idx += 1 
        return result



        


def delimeter_maker(length):
    return f"#${length}^%#"

def is_delimeter(string):
    if len(string) < 6: return False , 0 
    first = string[:2]
    number = string[2:len(string)- 3 ]
    second = string[len(string)- 3: ]

    if first != "#$": return False, 0 
    if second != "^%#": return False, 0 
    try:
        number = int(number)
    except Exception as e:
        return False, 0 

    return True ,number

