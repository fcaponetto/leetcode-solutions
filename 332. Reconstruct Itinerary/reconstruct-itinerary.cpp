// 332. Reconstruct Itinerary (9/29/55432)
// Runtime: 20 ms (31.08%) Memory: 16.66 MB (94.73%) 

class Solution {
public:
    vector<string> findItinerary(vector<vector<string>> tickets)
    {
        // // Sort destination in lexical order
        // sort(tickets.begin(), tickets.end(),
        //      [] (const auto &lhs, const auto &rhs) { return lhs[1] < rhs[1]; });

        for (auto e : tickets)
            graph[e[0]].push(e[1]);
        dfs("JFK");

        reverse(result.begin(), result.end());
        return result;
    }

private:
    void dfs(string vtex)
    {
        auto & edges = graph[vtex];
        while (!edges.empty())
        {
            string to_vtex = edges.top();
            edges.pop();
            dfs(to_vtex);
        }
        result.push_back(vtex);
    }

    unordered_map<string, std::priority_queue<string, vector<string>, greater<string>>> graph;
    vector<string> result;
};