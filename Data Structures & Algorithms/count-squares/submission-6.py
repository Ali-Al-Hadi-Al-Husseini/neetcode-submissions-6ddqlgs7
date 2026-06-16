class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        
    def count(self, point: List[int]) -> int:
       
        squares = 0
        for curr_point in self.points:
            curr_squares = self.sqauare_count(point,curr_point)
            squares +=  curr_squares  * self.points[curr_point]

        return squares

    def sqauare_count(self,point1,point2):
        i,j = point1
        x,y = point2 
        if i == x:
            return 0
        if (i,y)in self.points and (x,j) in self.points and abs(i-x) == abs(y-j):
            return self.points[(i,y)] * self.points[(x,j)]
        return 0