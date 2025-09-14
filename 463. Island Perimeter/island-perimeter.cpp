// 463. Island Perimeter (11/25/57673)
// Runtime: 49 ms (1.16%) Memory: 118.23 MB (0.00%) 

/*
* Time complexity O(n * m)
* Space complexity O(n * m)
*/

class Solution {
struct Cell
{
    int x;
    int y;

    bool operator<(const Cell& other) const
    {
        if(x != other.x) return x < other.x;
        return y < other.y;
    }
};
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        ROWS = grid.size();
        COLS = grid[0].size();

        for(int i=0; i < ROWS; i++)
        {
            for(int j=0; j < COLS; j++)
            {
                if(grid[i][j] == 1)
                {
                    return bfs(grid, {i, j});
                }
            }
        }

        return 0;
    }

    int bfs(const auto& grid, const Cell& start)
    {
        frontier.push(start);
        processed.insert(start);

        int perimeter = 0;
        while(! frontier.empty())
        {
            const auto curr = frontier.front(); frontier.pop();

            for(const auto& [dx, dy] : DIRS)
            {
                const Cell next{curr.x + dx, curr.y + dy};
                if(next.x >=0 && next.x < ROWS
                && next.y >=0 && next.y < COLS
                && processed.find(next) == processed.end()
                && grid[next.x][next.y] == 1)
                {
                    frontier.push(next);
                    processed.insert(next);
                }
                else if(next.x < 0 || next.x >= ROWS 
                    || next.y < 0 || next.y >= COLS 
                    || grid[next.x][next.y] == 0)
                {
                // Everything else contributes to perimeter:
                // - Out of bounds
                // - Water cells (grid[x][y] == 0)  
                    perimeter++;
                }
            }
        }

        return perimeter;
    }

private:
    int ROWS;
    int COLS;

    std::vector<Cell> DIRS = {{1, 0}, {0, -1}, {-1, 0}, {0, 1}};

    std::queue<Cell> frontier;
    std::set<Cell> processed;
};