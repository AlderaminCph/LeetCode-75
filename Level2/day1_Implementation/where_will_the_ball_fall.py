"""
You have a 2-D grid of size m x n representing a box, and you have n balls.
The box is open on the top and bottom sides.

Each cell in the box has a diagonal board spanning two corners of the cell that
 can redirect a ball to the right or to the left.

    A board that redirects the ball to the right spans the top-left corner to
    the bottom-right corner and is represented in the grid as 1.
    A board that redirects the ball to the left spans the top-right corner to
    the bottom-left corner and is represented in the grid as -1.

We drop one ball at the top of each column of the box. Each ball can get stuck
in the box or fall out of the bottom. A ball gets stuck if it hits a "V" shaped
 pattern between two boards or if a board redirects the ball into either wall
 of the box.

Return an array answer of size n where answer[i] is the column that the ball
falls out of at the bottom after dropping the ball from the ith column at the
top, or -1 if the ball gets stuck in the box.



Example 1:

>>> Solution().findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],\
[1,1,1,1,-1],[-1,-1,-1,-1,-1]])
[1, -1, -1, -1, -1]

Explanation: This example is shown in the photo.
Ball b0 is dropped at column 0 and falls out of the box at column 1.
Ball b1 is dropped at column 1 and will get stuck in the box between column 2
and 3 and row 1.
Ball b2 is dropped at column 2 and will get stuck on the box between column 2
and 3 and row 0.
Ball b3 is dropped at column 3 and will get stuck on the box between column 2
and 3 and row 0.
Ball b4 is dropped at column 4 and will get stuck on the box between column 2
and 3 and row 1.

Example 2:

>>> Solution().findBall([[-1]])
[-1]

Explanation: The ball gets stuck against the left wall.

Example 3:

>>> Solution().findBall([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],\
[-1,-1,-1,-1,-1,-1]])
[0, 1, 2, 3, 4, -1]
"""
from typing import List
import doctest


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        m = len(grid)
        ans = []
        for i in range(n):
            k = 0
            j = i
            f = 0
            while k < m:
                if j == n - 1 and grid[k][j] == 1:
                    f = 1
                    break
                elif j == 0 and grid[k][j] == -1:
                    f = 1
                    break
                elif grid[k][j] == 1 and j + 1 < n and grid[k][j + 1] == -1:
                    f = 1
                    break
                elif grid[k][j] == -1 and j - 1 >= 0 and grid[k][j - 1] == 1:
                    f = 1
                    break
                if grid[k][j] == 1:
                    j += 1
                else:
                    j -= 1
                k += 1
            if f:
                ans.append(-1)
            else:
                ans.append(j)
        return ans


doctest.testmod()
