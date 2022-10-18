"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and
'0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        # get the dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        # mark positions ourselves visited
        visit = set()
        # the number of islands
        islands = 0

        def bfs(r, c):
            q = deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                # 4 directions
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (
                        (r) in range(rows)
                        and (c) in range(cols)
                        and grid[r][c] == "1"
                        and (r, c) not in visit
                    ):
                        q.append((r, c))
                        visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    # run breadth first search
                    bfs(r, c)
                    islands += 1
        return islands
