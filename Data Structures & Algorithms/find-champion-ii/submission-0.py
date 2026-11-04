class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        points_to_edge = [True for _ in range(n)]

        for u,v in edges:
            points_to_edge[v] = False

        possible_champ = []
        for ver,points in enumerate(points_to_edge):
            if points:
                possible_champ.append(ver)

        return possible_champ[0] if len(possible_champ) < 2 else -1

        