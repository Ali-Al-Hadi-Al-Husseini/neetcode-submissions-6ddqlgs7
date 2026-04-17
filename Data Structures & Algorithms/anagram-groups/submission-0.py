class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_hash = {}

        for string in strs:
            string_tuple = get_str_tuple(string)
            if string_tuple not in strs_hash:
                strs_hash[string_tuple] = []


            strs_hash[string_tuple].append(string)

        return [value for value in strs_hash.values()]



def get_str_tuple(string):
    _chars = [0 for _ in range(27)]

    for _chr in string:
        _chars[ord('a') - ord(_chr)] += 1

    return tuple(_chars)