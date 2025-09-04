// 200. Number of Islands (2/28/57641)
// Runtime: 72 ms (2.76%) Memory: 23.16 MB (31.07%) 

#include <queue>

class Solution {
struct Cell
{
    int x;
    int y;

    bool operator==(const Cell& other) const
    {
        return x == other.x and y == other.y;
    }

    bool operator<(const Cell& other) const
    {
        if(x != other.x) return x < other.x;
        return y < other.y;
    }
};

public:
    int numIslands(vector<vector<char>>& grid) {
        ROWS = grid.size();
        COLS = grid[0].size();

        // bfs(grid, {0,0});
        // bfs(grid, {0, COLS-1});
        // bfs(grid, {ROWS-1, 0});
        // bfs(grid, {ROWS-1, COLS-1});

        int islandsCount = 0;
        for(int i = 0; i < ROWS; ++i)
        {
            for(int j = 0; j < COLS; ++j)
            {
                if(grid[i][j] == '1' && processed.find({i,j}) == processed.end())
                {
                    bfs(grid, {i,j});
                    islandsCount++;
                }
            }
        }


        return islandsCount;
    }

    void bfs(const auto& grid, const Cell& start)
    {
        frontier.push(start);
        processed.insert(start);

        while(!frontier.empty())
        {
            const auto curr = frontier.front(); frontier.pop();

            for(const auto [dx, dy] : directions)
            {
                const Cell next= {curr.x + dx, curr.y + dy};

                if(next.x >= 0 && next.x < ROWS and next.y >=0 and next.y < COLS
                  && processed.find(next) == processed.end()
                  && grid[next.x][next.y] == '1')
                {
                    frontier.push(next);
                    processed.insert(next);
                }
            }
        }
        
    }

private:
    std::vector<Cell> directions = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    std::set<Cell> processed;
    std::queue<Cell> frontier;

    int ROWS;
    int COLS;
};