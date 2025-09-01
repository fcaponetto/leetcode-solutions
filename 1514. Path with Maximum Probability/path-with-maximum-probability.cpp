// 1514. Path with Maximum Probability (7/7/57639)
// Runtime: 71 ms (14.48%) Memory: 77.79 MB (1.10%) 

/*
*   Time complexity: O(E * log V)
        E heap push -> O(E * log E)
        V heap pop -> O(V * log V)
    
    Space complexity: O(E + V)
        E adjacent list
        V probabilities so far
        E frontier 
*/

#include <deque>

class Solution {
struct Edge
{
    int to;
    double prob;

    // For max-heap behavior (larger prob has higher priority)
    bool operator<(const Edge& other) const
    {
        return prob < other.prob;
    }
};

public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start_node, int end_node) {
        for(int i=0; i < edges.size(); ++i)
        {
            const auto from = edges[i][0];
            const auto to = edges[i][1];
            const auto prob = succProb[i];
            //  Add both directions (assuming undirected graph)
            adjList[from].push_back({to, prob});
            adjList[to].push_back({from, prob});
        }

        frontier.push({start_node, 1.0});
        prob_so_far[start_node] = 1.0;

        while(!frontier.empty())
        {
            // current edge
            const auto curr = frontier.top(); frontier.pop();

            // If we reached the destination, return the probability
            // Dijskstra returns the best path, so the curr already
            // incorporates the best probability.
            if(curr.to == end_node)
            {
                return curr.prob;
            }

            // if the current node has been already processed and
            // it could be reached with higher probability, then skip it
            if(curr.prob < prob_so_far[curr.to])
            {
                continue;
            }

            const auto& it = adjList.find(curr.to);
            if(it != adjList.end())
            {
                for(const auto& edge : it->second)
                {
                    const auto newProb = curr.prob * edge.prob;
                    if(prob_so_far.find(edge.to) == prob_so_far.end() || 
                        prob_so_far.at(edge.to) < newProb)
                    {
                        frontier.push({edge.to, newProb});
                        prob_so_far[edge.to] = newProb;
                    }
                }
            }
        }

        return 0.0;
    }

private:
    std::unordered_map<int, std::vector<Edge>> adjList;
    std::unordered_map<int, double> prob_so_far;
    std::priority_queue<Edge, std::vector<Edge>, std::less<Edge>> frontier;
};