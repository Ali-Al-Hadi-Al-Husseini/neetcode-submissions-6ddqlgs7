class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list= defaultdict(set)
        dependices = defaultdict(int)
        chars = set("".join(words))

        for idx in range(1,len(words)):
            prev_word = words[idx -1]
            curr_word = words[idx]

            i,j = 0,0
        
            while i < len(prev_word) and j <len(curr_word) and  prev_word[i] == curr_word[j]:
                i += 1
                j += 1

            if i == len(prev_word):
                continue
            if j == len(curr_word):
                if len(prev_word) > len(curr_word) :
                    return ""
                continue
            if curr_word[j] in adj_list[prev_word[i]]:
                continue
            adj_list[prev_word[i]].add(curr_word[j])
            dependices[curr_word[j]] += 1 

        def bfs():
            res = ""
            queue = deque()
            visited = set()

            for _chr in chars:
                if dependices[_chr] == 0:
                    res += _chr
                    queue.append(_chr)

            while queue:
                curr_chr = queue.popleft()
                if dependices[curr_chr] == -1:
                    continue
                dependices[curr_chr] = -1

                for neighbor in adj_list[curr_chr]:
                    dependices[neighbor] -= 1
                    if dependices[neighbor]  <= 0:
                        res += neighbor
                        queue.append(neighbor)
            return res

        res = bfs()
        return res if len(res) == len(chars) else ""
