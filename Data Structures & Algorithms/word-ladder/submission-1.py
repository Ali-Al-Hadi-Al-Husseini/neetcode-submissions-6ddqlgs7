class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj_list = defaultdict(list)
        wordList.append(beginWord)

        for idx in range(len(wordList)):
            node = wordList[idx]
            for j in range(idx +1, len(wordList)):
                neigh = wordList[j]
                if is_neighbor(node,neigh):
                    adj_list[node].append(neigh)
                    adj_list[neigh].append(node)

        queue = deque()
        min_dist = float("+inf")
        queue.append((beginWord,1))
        visited = set()

        while queue:
            curr_node, dist = queue.popleft()

            for neigh in adj_list[curr_node]:
                if neigh  == endWord:
                    min_dist = min(min_dist, dist + 1)
                if neigh in visited:
                    continue
                queue.append((neigh,dist+1))

            visited.add(curr_node)

        return min_dist if min_dist != float("+inf") else 0 






def is_neighbor(word1,word2):
    differnce = 0
    
    for idx in range(len(word1)):
        if word1[idx] != word2[idx]:
            differnce += 1 

    return differnce <= 1 