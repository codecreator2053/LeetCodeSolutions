class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        res = []
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        direc = 0
        x,y = 0,0
        corners = [0, n-1, 0, m-1]
        while(corners[0]<=corners[1] and corners[2]<=corners[3]):
            for i in range(corners[2], corners[3]+1):
                res.append(matrix[corners[0]][i])
            corners[0]+=1
            
            for i in range(corners[0], corners[1]+1):
                res.append(matrix[i][corners[3]])
            corners[3]-=1

            if corners[0]<=corners[1]:
                for i in range(corners[3], corners[2]-1, -1):
                    res.append(matrix[corners[1]][i])
            corners[1]-=1
            
            if corners[2]<=corners[3]:
                for i in range(corners[1], corners[0]-1, -1):
                    res.append(matrix[i][corners[2]])
                corners[2]+=1

        return res

