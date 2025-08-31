// 1091. Shortest Path in Binary Matrix (2/18/57636)
// Runtime: 794 ms (0.00%) Memory: 36.94 MB (10.12%) 

#include <queue>

class Solution {

struct Cell
{
    int x;
    int y;
};

public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        const auto N = grid.size();
        const auto M = grid[0].size();

        // the top-left cell is occupied
        if(grid[0][0] == 1 or grid[N-1][M-1] == 1)
        {
            return -1;
        }

        std::set<std::pair<int, int>> processed;
        std::queue<Cell> frontier;

        frontier.push({0,0});
        processed.insert({0,0});

        auto length = 1;
        while(not frontier.empty())
        {
            // Process all the nodes at the current level
            const auto curr_frontier_size = frontier.size();
            for(int i = 0; i < curr_frontier_size; ++i)
            {
                const auto curr = frontier.front(); frontier.pop();

                // if the bottom-right cell, then we arrived
                std::cout << curr.x << " " << curr.y << std::endl;
                if (curr.x == N - 1 and curr.y == M -1)
                    return length;

                for (const auto& [dx, dy] : motions)
                {
                    const Cell next({curr.x + dx, curr.y + dy});
                    if(isWithinBoundaries(N, M, next)
                    and (processed.find({curr.x + dx, curr.y + dy}) == processed.end()) 
                    and !isObstacle(grid, next))
                    {
                        processed.insert({next.x, next.y});
                        frontier.push(next);
                    }
                }
            }
            length += 1;
        }

        return -1;
    }

private:
    std::vector<Cell> motions = {{-1,0}, {-1,1}, {0,1}, {1,1}, {1,0}, {1,-1}, {0,-1}, {-1,-1}};

    bool isObstacle(const std::vector<std::vector<int>>& grid, const Cell& cell)
    {
        return grid[cell.x][cell.y] == 1;
    }

    bool isWithinBoundaries(const int ROWS, const int COLS, const Cell& cell)
    {
        return (cell.x >= 0 && cell.x < ROWS && cell.y >= 0 && cell.y < COLS);
    }
};