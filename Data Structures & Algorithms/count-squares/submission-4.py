class CountSquares:

    def __init__(self):
        self.points_count = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.points_count[tuple(point)] += 1
        self.points.append(tuple(point))
    
        
    def count(self, point: List[int]) -> int:
        squares = 0
        i,j = point
        for x,y in self.points:
            if abs(i-x) != abs(y-j) or x== i or j == y :
                continue
            squares += self.points_count[(x,j)] * self.points_count[(i,y)]
        return squares

