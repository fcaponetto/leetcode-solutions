// 417. Pacific Atlantic Water Flow (12/20/57662)
// Runtime: 36 ms (8.96%) Memory: 25.76 MB (19.15%) 

/*
*   Time complexity: O(n * m) -> in the worst case, the expantion goes from the border to the other one
    Space complexity: O(n * m) -> same as above
*/ 


#include<array>

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
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        ROWS = heights.size();
        COLS = heights[0].size();

      // Identify Pacific top border and Atlantic bottom border
        for (int i = 0; i < COLS; i++) {
            frontier_pacific.push({0, i});
            frontier_atlantic.push({ROWS - 1, i});
        }

        // Identify Pacific left border and Atlantic right border
        for (int i = 0; i < ROWS; i++) {
            frontier_pacific.push({i, 0});
            frontier_atlantic.push({i, COLS - 1});
        }

        bfs(heights, frontier_pacific, processed_pacific);
        bfs(heights, frontier_atlantic, processed_atlantic);


        std::vector<vector<int>> coordinates;
        for(const auto& pac_cell : processed_pacific)
        {
            if (processed_atlantic.find(pac_cell) != processed_atlantic.end())
            {
                coordinates.push_back({pac_cell.x, pac_cell.y});
            }
        }
        return coordinates;
    }

private:

    void bfs(const auto& grid, auto& frontier, auto& processed)
    {
        while(! frontier.empty())
        {
            const auto curr = frontier.front(); frontier.pop();

            // CRITICAL: Mark current cell as processed FIRST
            // NOTE: This includes border cells and "dead ends" that may not reach the other ocean
            // For example, (0,0) gets added to processed_pacific even if it can't reach Atlantic
            // The final intersection step filters out cells that can't reach both oceans
            processed.insert(curr);

            for(const auto& [dx, dy] : DIRS)
            {
                const Cell next{curr.x + dx, curr.y + dy};

                if(next.x >= 0 && next.x < ROWS
                && next.y >= 0 && next.y < COLS
                && processed.find(next) == processed.end()
                && grid[next.x][next.y] >= grid[curr.x][curr.y])
                {
                    frontier.push(next);
                }
            }
        }
    }

    int ROWS;
    int COLS;

    std::vector<Cell> DIRS = {{1,0}, {0,-1}, {-1,0}, {0,1}};

    std::queue<Cell> frontier_pacific;
    std::queue<Cell> frontier_atlantic;
    std::set<Cell> processed_pacific;
    std::set<Cell> processed_atlantic;
};