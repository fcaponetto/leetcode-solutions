// 1091. Shortest Path in Binary Matrix (4/18/57655)
// Runtime: 54 ms (13.05%) Memory: 25.77 MB (42.04%) 

/*
* Time Complexity
    Total: O(V) × O(log V) + O(E) × O(log V) = O((V + E) log V)
    In dense grids: E = O(V), so this becomes O(V log V)
  Space complexity O(V)
*/

#include <queue>
#include <array>

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
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {

        ROWS = grid.size();
        COLS = grid.size();

        if(grid[0][0] == 1 || grid[ROWS-1][COLS-1] == 1)
        {
            return -1;
        }

        const Cell goal{ROWS-1, COLS-1};
        const Cell start{0, 0};
        return a_star(grid, start, goal);
    }

private:

    int heuristic(const Cell& start, const Cell& end)
    {
        return std::max(std::abs(start.x - end.x), std::abs(start.y - end.y));
    }

    int a_star(const auto& grid, const Cell& start, const Cell& goal)
    {
        frontier.push({0, start});
        distance_so_far[start] = 1;
        // processed.insert(start);

        while(! frontier.empty()) // O(V) operations
        {
            const auto [_,curr] = frontier.top(); frontier.pop(); // O(log V)
            
            if(curr.x == goal.x && curr.y == goal.y)
                return distance_so_far[curr];

            for (const auto& [dx, dy] : DIRS) // O(E) operations
            {
                const Cell next{curr.x + dx, curr.y + dy};
                const auto new_distance = distance_so_far[curr] + 1;

                if(next.x >= 0 && next.x < ROWS
                && next.y >= 0 && next.y < COLS
                && grid[next.x][next.y] != 1
                && (distance_so_far.find(next) == distance_so_far.end() || distance_so_far[next] > new_distance))
                {
                    distance_so_far[next] = new_distance;
                    const auto priority = new_distance + heuristic(next, goal);

                    frontier.push({priority, next}); // O(log V) operations
                }

            }
        }

        return -1;
    }

    int ROWS;
    int COLS;

    std::vector<Cell> DIRS = {{1,0}, {1,-1}, {0,-1}, {-1,-1},{-1,0}, {-1,1}, {0,1}, {1,1}};

    // std::set<Cell> processed;

    using PriorityCell = std::pair<int, Cell>;
    std::priority_queue<PriorityCell, std::vector<PriorityCell>, std::greater<PriorityCell>> frontier;
    std::map<Cell, int> distance_so_far;

};


/// BFS implementation

// class Solution {

// struct Cell
// {
//     int x;
//     int y;
// };

// public:
//     int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
//         const auto N = grid.size();
//         const auto M = grid[0].size();

//         // the top-left cell is occupied
//         if(grid[0][0] == 1 or grid[N-1][M-1] == 1)
//         {
//             return -1;
//         }
//
//         std::set<std::pair<int, int>> processed;
//         std::queue<Cell> frontier;

//         frontier.push({0,0});
//         processed.insert({0,0});

//         auto length = 1;
//         while(not frontier.empty())
//         {
//             // Process all the nodes at the current level
//             const auto curr_frontier_size = frontier.size();
//             for(int i = 0; i < curr_frontier_size; ++i)
//             {
//                 const auto curr = frontier.front(); frontier.pop();

//                 // if the bottom-right cell, then we arrived
//                 std::cout << curr.x << " " << curr.y << std::endl;
//                 if (curr.x == N - 1 and curr.y == M -1)
//                     return length;

//                 for (const auto& [dx, dy] : motions)
//                 {
//                     const Cell next({curr.x + dx, curr.y + dy});
//                     if(isWithinBoundaries(N, M, next)
//                     and (processed.find({curr.x + dx, curr.y + dy}) == processed.end()) 
//                     and !isObstacle(grid, next))
//                     {
//                         processed.insert({next.x, next.y});
//                         frontier.push(next);
//                     }
//                 }
//             }
//             length += 1;
//         }

//         return -1;
//     }

// private:
//     std::vector<Cell> motions = {{-1,0}, {-1,1}, {0,1}, {1,1}, {1,0}, {1,-1}, {0,-1}, {-1,-1}};

//     bool isObstacle(const std::vector<std::vector<int>>& grid, const Cell& cell)
//     {
//         return grid[cell.x][cell.y] == 1;
//     }

//     bool isWithinBoundaries(const int ROWS, const int COLS, const Cell& cell)
//     {
//         return (cell.x >= 0 && cell.x < ROWS && cell.y >= 0 && cell.y < COLS);
//     }
// };