// 341. Flatten Nested List Iterator (4/14/54326)
// Runtime: 26 ms (0.00%) Memory: 15.08 MB (94.62%) 

/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */

class NestedIterator {
public:
    NestedIterator(vector<NestedInteger> &_nl) 
    {
        for(int i = _nl.size()-1; i>= 0; i--)
            nodes_.push(_nl[i]);
    }
    
    int next() 
    {
        const int ret = nodes_.top().getInteger();
        nodes_.pop();
        return ret; 
    }
    
    bool hasNext() 
    {
        while(!nodes_.empty())
        {
            NestedInteger curr = nodes_.top();
            
            if(curr.isInteger())
                return true;
            
            nodes_.pop();

            std::vector<NestedInteger> nestedList = curr.getList();
            for(int i = nestedList.size()-1; i>=0; i--)
            {
                nodes_.push(nestedList[i]);
            }
            
        }
        return false;
        
    }
    
private:
    std::stack<NestedInteger> nodes_;
};


/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */