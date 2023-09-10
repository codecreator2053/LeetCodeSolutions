DFS solution with recursion, Time complexity: O(n), Space complexity: O(1), memory used O(MN * memory for each call)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        def changeFrom(i, j):
            if i<0 or j<0 or i<len(grid) or j<len(grid[0]) or grid[i][j]!="!":
                return 
            grid[i][j] = "0"
            changeFrom(i+1, j)
            changeFrom(i, j+1)
            changeFrom(i-1, j)
            changeFrom(i, j-1)
        
        numIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    numIslands+=1
                    changeFrom(i, j)
        return numIslands


BFS solution with collections.queue(), Time complexity: 
class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def isValid(m, n):
            if m<0 or n<0 or m>=len(grid) or n>=len(grid[0]):
                return False
            else:
                return True
        
        
        def changeFrom(i, j):
            queue = collections.deque()
            d = [[1,0], [0, 1], [-1, 0], [0, -1]]
            queue.append((i,j))
            grid[i][j]="0"
            while queue:
                m, n = queue.popleft()
                for k in d:
                    if isValid(m+k[0], n+k[1]) and grid[m+k[0]][n+k[1]]=="1":
                        queue.append((m+k[0], n+k[1]))
                        grid[m+k[0]][n+k[1]]="0"
            
        
        numIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    numIslands+=1
                    changeFrom(i, j)
        return numIslands