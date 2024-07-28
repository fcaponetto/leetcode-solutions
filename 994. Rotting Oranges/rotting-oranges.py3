# 994. Rotting Oranges (9/7/56543)
# Runtime: 44 ms (83.39%) Memory: 16.56 MB (28.47%) 

# Time complexity O(n * m)
# Space complexity O(n * m)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # needed to know where to start the BFS from
        def findRottenAndCountFresh():
            rottenOranges = []
            fresh = 0
            for i in range(ROWS):
                for j in range(COLS):
                    if grid[i][j] == 2:
                        rottenOranges.append((i,j))
                    if grid[i][j] == 1:
                        fresh += 1
            return rottenOranges, fresh

        def bfs(rottens, fresh):
            mins = 0
            directions = [[1,0], [0, 1], [-1, 0], [0, -1]]
            frontier = deque(rottens)

            while frontier:
                size = len(frontier)
                new_rotten = False
                # mins is incremented each time a new orange is rotted, but it should only be 
                # incremented once per minute (i.e., once per level of BFS traversal).
                for _ in range(size):
                    r, c = frontier.popleft()

                    for dr, dc in directions:
                        new_r, new_c = r + dr, c + dc

                        if (0 <= new_r < ROWS and
                            0 <= new_c < COLS and
                            grid[new_r][new_c] == 1):
                            
                            grid[new_r][new_c] = 2 # if we are allowed to change the grid, we don't need visited
                            frontier.append((new_r, new_c))
                            new_rotten = True
                            fresh -= 1

                if new_rotten:
                    mins +=1

            # Check if at least one fresh orange left in the grid
            return mins if fresh == 0 else -1

        rottens, fresh = findRottenAndCountFresh()
        mins = bfs(rottens, fresh)
        return mins
