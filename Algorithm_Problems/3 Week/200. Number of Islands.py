"""
Runtime: 140 ms, faster than 74.09% of Python3 online submissions for Number of Islands.
Memory Usage: 15.6 MB, less than 37.73% of Python3 online submissions for Number of Islands.
"""

"""
접근 전략
- 한번 방문한 곳이 섬이라면 섬을 모두 돌아다니며 섬이 아니라고 표기한 뒤 섬을 탈출
- 각 그리드를 모두 탐색하며 섬을 발견하면 섬! 카운트를 세고 돌아다니며(사방을 봄) 다 지움
- 제귀를 사용하며 지도 밖으로 나가거나 섬이 아닌 곳을 밟을 경우 종료
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
#         self.print_map(grid)
        island_count = 0
        def dfs(i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1":
                return
            else:
                grid[i][j] = "@"
                dfs(i-1,j)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i,j+1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    island_count+=1
                    dfs(i,j)
#         self.print_map(grid)
        return island_count
    
#     @staticmethod
#     def print_map(grid):
#         for line in grid:
#             print(*line)       
#         print()
        
"""print_map결과
grid_before
1 1 1 1 0
1 1 0 1 0
1 1 0 0 0
0 0 0 0 0

grid_after 
@ @ @ @ 0
@ @ 0 @ 0
@ @ 0 0 0
0 0 0 0 0

"""
