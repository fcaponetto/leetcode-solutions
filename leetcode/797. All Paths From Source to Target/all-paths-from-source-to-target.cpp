// 797. All Paths From Source to Target (6/2/55336)
// Runtime: 7 ms (74.99%) Memory: 10.67 MB (94.98%) 

// Since we have a DAG, we won't visit a node multiple time.
// Thus, we don't have to keep the processed structure
void dfs(const std::vector<std::vector<int>>& g, const int curr, std::vector<std::vector<int>>& paths, std::vector<int>& path)
{
    path.push_back(curr);
    
    // if the end
    if(curr == g.size() - 1)
    {
        paths.push_back(path);
        return;
    }
    
    for(const auto& next : g[curr])
    {
        dfs(g, next, paths, path);
        path.pop_back();
    }
    
}

class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) 
    {
        std::vector<std::vector<int>> paths;
        std::vector<int> path;
        
        dfs(graph, 0, paths, path);
        
        return paths;
    }
};
