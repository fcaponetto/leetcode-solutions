// 695. Max Area of Island (7/17/57643)
// Runtime: 23 ms (1.68%) Memory: 30.62 MB (22.98%) 

#include <queue>

class Solution {
struct Cell
{
    int x;
    int y;

    bool operator<(const Cell& other) const
    {
        if (x != other.x) return x < other.x;
        return y < other.y; 
    }
};

public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        ROWS = grid.size();
        COLS = grid[0].size();

        int maxArea = 0;
        for(int i = 0; i < ROWS; i++)
        {
            for(int j = 0; j < COLS; j++)
            {
                if(grid[i][j] == 1
                  && processed.find({i,j}) == processed.end())
                {
                    const auto area = bfs(grid, {i, j});
                    maxArea = std::max(maxArea, area);
                }
            }
        }
        return maxArea;
    }

    int bfs(const auto& grid, const Cell& start)
    {
        frontier.push(start);
        processed.insert(start);

        int area = 0;
        while(!frontier.empty())
        {
            const auto curr = frontier.front(); frontier.pop();
            area++;

            for(const auto& [dx, dy] : directions)
            {
                const Cell next{curr.x + dx, curr.y + dy};

                if(next.x >= 0 && next.x < ROWS && 
                   next.y >= 0 && next.y < COLS &&
                   processed.find(next) == processed.end()&& 
                   grid[next.x][next.y] == 1)
                {
                    frontier.push(next);
                    processed.insert(next);
                }
            }
        }
        return area;
    }

private:
    int ROWS;
    int COLS;

    std::vector<Cell> directions = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

    std::queue<Cell> frontier;
    std::set<Cell> processed;
};