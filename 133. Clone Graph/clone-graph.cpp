// 133. Clone Graph (2/3/55163)
// Runtime: 3 ms (64.32%) Memory: 8.75 MB (94.66%) 

/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) 
    {
        if(node == nullptr)
            return node;
        
        Node *copy = new Node;
        dfs(node, copy);
        
        return copy;
    }

private:
std::unordered_map<int, Node*> processed;
void dfs(Node * original, Node *copy)
{
    // if already processed, skip it
    if(processed.find(original->val) != processed.end())
    {
        return;
    }
    
    processed[original->val] = copy;
    copy->val = original->val;
    
    for(Node* originalNext : original->neighbors)
    {
        Node *copyNext;
        
        if(processed.find(originalNext->val) == processed.end())
            copyNext = new Node;
        else
            copyNext = processed[originalNext->val];
        
        copy->neighbors.push_back(copyNext);
        dfs(originalNext, copyNext);
    }
}
};