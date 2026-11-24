class DSU:
    def __init__(self,size):
        self.parents = [-1] * size
        self.parent_num = size

    def find_parent(self,node):
        if self.parents[node] >= 0 :
            parent = self.find_parent(self.parents[node])
            self.parents[node] = parent
            return parent
        return node

    def union(self,u,v):
        pu = self.find_parent(u)
        pv = self.find_parent(v)

        if pu == pv :
            return False

        if self.parents[pv] < self.parents[pu]:
            self.parents[pv] += self.parents[pu]
            self.parents[pu] = pv 
        else:
            self.parents[pu] += self.parents[pv]
            self.parents[pv] = pu
        self.parent_num  -=1
        return False


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        dsu = DSU((m *n))

        def linear_idx(row,col):
            return (row * n ) + col

        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "0":
                    dsu.parent_num -= 1
                    continue


                for rs,cs in directions:                
                    new_row = r + rs
                    new_col = c + cs

                    in_bounds = n > new_col >= 0 and m > new_row >= 0
                    if not in_bounds or grid[new_row][new_col] == "0" :
                        continue
                    
                    dsu.union(linear_idx(new_row,new_col), linear_idx(r,c))
                        

        return dsu.parent_num

                    



        

