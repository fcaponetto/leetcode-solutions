// 874. Walking Robot Simulation (11/30/57677)
// Runtime: 27 ms (59.85%) Memory: 37.83 MB (55.96%) 

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
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {

        for(const auto& o : obstacles)
        {
            {
                obst.insert({o[0], o[1]});
            }
        }

        const auto COMM_SIZE = commands.size();
        
        int maxDistanceSquared = 0;

        int dir = 0;
        Cell curr{0,0};
        bool start = true;

        for(const auto& command: commands)
        {
            if(command == -1)
            {
                dir = ++dir % 4; // turn right
                continue;
            }
            if(command == -2)
            {
                dir = (--dir + 4) % 4; // turn left
                continue;
            }

            if(command >= 1 && command <=9)
            {
                for(int i=0; i < command; ++i)
                {
                    const auto& [dx, dy] = DIRS[dir];
                    const Cell next{curr.x + dx, curr.y + dy};

                    // if not running into obstacle, then increment the cell
                    if(obst.find(next) == obst.end())
                    {
                        curr = next;

                        // Update max distance squared at each step
                        int currentDistSq = curr.x * curr.x + curr.y * curr.y;
                        maxDistanceSquared = std::max(maxDistanceSquared, currentDistSq);
                    }
                    else
                    {
                        break;
                    }
                }
            }
        }

        return maxDistanceSquared;
    }

private:
    std::vector<Cell> DIRS = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    // std::set<Cell> processed;

    std::set<Cell> obst;
};