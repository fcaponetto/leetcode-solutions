// 1971. Find if Path Exists in Graph (4/27/55279)
// Runtime: 628 ms (34.69%) Memory: 161.30 MB (71.78%) 

class Graph
{
public:
    Graph(const int size)
    {
        adj.resize(size);
    }

    void addEdge(const int src, const int dst)
    {
        adj[src].push_back(dst);
    }

    std::vector<int> getNeighboors(const int node) const
    {
        return adj[node];
        // if(adj.find(node) != adj.end())
        // {
        //     return adj.at(node);
        // }
        // return {};
    }

    int getNumNodes() const
    {
        return adj.size();
    }

private:
    std::vector<std::vector<int>> adj;
    // std::unordered_map<int, std::vector<int>> adj;
};


bool dfs(const Graph& graph, const int src, const int dst)
{
    std::vector<bool> processed(graph.getNumNodes());
    std::stack<int> frontier;

    processed[src] = true;
    frontier.push(src);

    while (!frontier.empty()) 
    {
        const int current = frontier.top(); frontier.pop();

        if(current == dst)
            return true;
        for (const auto next: graph.getNeighboors(current))
        {
            if(!processed[next])
            {
                processed[next] = true;
                frontier.push(next);
            }
        }
    }
    return false;
}


class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) 
    {
        if(n == 1)
            return true;
        Graph g(n);
        
        for(const auto& edge : edges)
        {
            g.addEdge(edge[0], edge[1]);
            g.addEdge(edge[1], edge[0]);
        }
        
        return dfs(g, source, destination);
    }
};