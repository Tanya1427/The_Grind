"""
733. Flood Fill
Solved
Easy
Topics
Companies
Hint
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

dfs - depth first search
bfs - breadth first search

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent
 (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and
 modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.

Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 2**16
0 <= sr < m
0 <= sc < n
"""

"""
UMPIRE
Understand:
image = 
[
    [1 1 1 3 1]
    [1 2 1 1 9]
    [1 1 2 2 3]
    [1 1 1 1 1]
    [3 1 1 1 1]
]
[
    [4 1 1 3 1]
    [4 2 1 1 9]
    [4 4 2 2 3]
    [4 4 4 4 1]
    [3 4 4 1 1]
]
[
    [4 4 4 3 1]
    [4 2 4 4 9]
    [4 4 2 2 3]
    [4 4 4 4 4]
    [3 4 4 4 4]
]
sr = 2
sc = 1
color = 4

Match:
Matrix. Arrays. Graphs. DFS.

Plan:
BASE_COLOR = image[sr][sc]

dfs(r, c)
    if direction not in bounds // value of direction not BASE_COLOR:
        return
    value of direction == color
    for direction in (top, right, down, left):
        dfs(direction.row, direction.column)

return image
    
"""

from typing import *

test = [
    [1, 1, 1, 3, 1],
    [1, 2, 1, 1, 9],
    [1, 1, 2, 2, 3],
    [1, 1, 1, 1, 1],
    [3, 1, 1, 1, 1],
]

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        BASE_COLOR = image[sr][sc]
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        m, n = len(image), len(image[0])

        if BASE_COLOR == color:
            return image

        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n) or image[r][c] != BASE_COLOR:
                return
            image[r][c] = color
            for delta in directions:
                dfs(r+delta[0], c+delta[1])

        dfs(sr, sc)

        return image
        


flood = Solution().floodFill()

print(flood(test))
def dfs(): pass
def main():
    ...
    ...

def nnn():  pass

if __name__ == "__main__":
    main()
