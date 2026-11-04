class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        is_weaker = [True for _ in range(n)]

        for u,v in edges:
            is_weaker[v] = False

        possible_champ = []
        for ver,points in enumerate(is_weaker):
            if points:
                possible_champ.append(ver)

        return possible_champ[0] if len(possible_champ) < 2 else -1

        