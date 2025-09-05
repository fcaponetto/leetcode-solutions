// 994. Rotting Oranges (7/10/57650)
// Runtime: 0 ms (93.76%) Memory: 16.78 MB (69.53%) 

/*
* Time complexity: O(N*M) (bfs O(V + E))
* Space complexity O(V) if all rottens
*/ 

class Solution {
struct Cell
{
    int x;
    int y;

    bool operator<(const Cell& other) const
    {
        if(x != other.x)  return x < other.x;
        return y < other.y;
    }
};

public:
    int orangesRotting(vector<vector<int>>& grid) {
        ROWS = grid.size();
        COLS = grid[0].size();

        bool availableFresh = false;
        for(int i = 0; i < ROWS; i++)
        {
            for(int j = 0; j < COLS; j++)
            {
                if(grid[i][j] == 2)
                {
                    frontier.push({i, j});
                    // processed.insert({i, j});
                }

                if(grid[i][j] == 1)
                {
                    availableFresh = true;
                }
            }
        }


        if(frontier.empty() && availableFresh)
        {
            return -1;
        }

        return bfs(grid);
    }

    int bfs(auto& grid)
    {
        int minutes = 0;

        while(! frontier.empty())
        {
            bool rottedThisRound = false;

            // Frontier is filled with rotten oranges
            // All sourranding oranges are affected at the same step
            // Thus, the same minute affects 
            const auto frontierSize = frontier.size();
            for (int i = 0; i < frontierSize; i++)
            {
                const auto curr = frontier.front(); frontier.pop();

                for(const auto& [dx, dy] : directions)
                {
                    const Cell next{curr.x + dx, curr.y + dy};

                    if(next.x >= 0 && next.x < ROWS && next.y >=0 && next.y < COLS
                    && grid[next.x][next.y] == 1)
                    // && processed.find(next) == processed.end()
                    {
                        grid[next.x][next.y] = 2;
                        frontier.push(next);
                        // processed.insert(next);
                        rottedThisRound = true;
                    }
                }
            }

            if(rottedThisRound) minutes++;
        }

        // check if there are left fresh oranges
        for(int i = 0; i < ROWS; i++)
        {
            for(int j = 0; j < COLS; j++)
            {
                if(grid[i][j] == 1) return -1;
            }
        }

        return minutes;
    }

private:
    int ROWS;
    int COLS;

    std::vector<Cell> directions = {{-1,0}, {0,1}, {1, 0}, {0, -1}};

    std::queue<Cell> frontier;
    // std::set<Cell> processed;
};