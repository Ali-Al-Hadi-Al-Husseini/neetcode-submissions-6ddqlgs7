class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list= defaultdict(set)
        dependices = defaultdict(int)
        chars = set("".join(words))

        for idx in range(1,len(words)):
            prev_word = words[idx -1]
            curr_word = words[idx]
            min_len = min(len(prev_word),len(curr_word))
            if len(prev_word) > len(curr_word) and prev_word[:min_len]== curr_word[:min_len]:
                return ""
        
            for idx in range(min_len):
                if prev_word[idx] !=curr_word[idx]:
                    if curr_word[idx] in adj_list[prev_word[idx]]: 
                        break
                    adj_list[prev_word[idx]].add(curr_word[idx])
                    dependices[curr_word[idx]] += 1 
                    break

        def bfs():
            res = ""
            queue = deque()

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
