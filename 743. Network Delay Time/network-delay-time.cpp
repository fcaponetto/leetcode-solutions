// 743. Network Delay Time (10/6/57636)
// Runtime: 101 ms (8.79%) Memory: 44.17 MB (78.11%) 

/*
*   Time Complexity: O(E * log V) 
        E heap pushed = O (E * log E)
        V heah pops = O (V * log V)
        ~ Total: O(E log V + V log V) = O(E log V) if E>V

    Space Complexity: O(V + E)
        E for the frontier (worst case)
        E adjacent list
        V for the cost tracking
*/

#include <queue>
#include <unordered_map>

class Solution {
struct Edge
{
    int to;
    int weight;

    bool operator()(const Edge& e1, const Edge& e2) const
    {
        return e1.weight < e2.weight;
    }
};

public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        for(const auto& edge : times)
        {
            const auto from = edge[0];
            const auto to = edge[1];
            const auto weight = edge[2];
            adjList[from].push_back({to, weight});
        }

        // push start node with zero cost 
        frontier.push({k, 0});
        cost_so_far[k] = 0;

        while(!frontier.empty())
        {
            // current edge
            const auto curr = frontier.top(); frontier.pop();

            // Skip if we've already found a better path to this node
            if(cost_so_far[curr.to] < curr.weight)
            {
                continue;
            }

            // for each adjacent node, keep track of the cost to reach it
            if (adjList.find(curr.to) != adjList.end()) 
            {
                // next edges
                for(const auto& next : adjList.at(curr.to))
                {
                    const auto new_cost = curr.weight + next.weight;
                    if (cost_so_far.find(next.to) == cost_so_far.end() || new_cost < cost_so_far[next.to])
                    {
                        cost_so_far[next.to] = new_cost;
                        frontier.push({next.to, new_cost});
                    }
                }
            }

        }

        // Check if all nodes are reachable
        if (cost_so_far.size() != n)
        {
            return -1;
        }

        // Dijkstra's algorithm finds the shortest path (minimum time) to reach each individual node.
        // Thus, we need to find when the last node receives the signal
        int maxTime = 0;
        for (const auto& [_, time] : cost_so_far)
        {
            maxTime = std::max(maxTime, time);
        }

        return maxTime;
    }

private:
    std::map<int, std::vector<Edge>> adjList;

    std::priority_queue<Edge, std::vector<Edge>, Edge> frontier;
    // <Node, time>
    std::unordered_map<int, int> cost_so_far; // it also keeps track of the visited nodes.
};