// 547. Number of Provinces (2/4/54992)
// Runtime: 25 ms (23.32%) Memory: 13.94 MB (94.91%) 

class DisjointSet
{
public:
    DisjointSet(const int size) : root(size), rank(size)
    {
        for(int i=0; i < size; i++)
        {
            root[i] = i;
            rank[i] = 1;
        }
    }

    int Find(const int x)
    {
        if( x == root[x])
        {
            return x;
        }
        return root[x] = Find(root[x]);
    }

    void Union(const int x, const int y)
    {
        const int rootX = Find(x);
        const int rootY = Find(y);

        if(rootX != rootY)
        {
            if(rank[rootX] > rank[rootY])
            {
                root[rootY] = rootX;
            }
            else if(rank[rootX] < rank[rootY])
            {
                root[rootX] = rootY;
            }
            else
            {
                root[rootY] = rootX;
                rank[rootX] += 1;
            }
        }
    }

    bool Connected(const int x, const int y)
    {
        return Find(x) == Find(y);
    }

private:
    std::vector<int> root;
    std::vector<int> rank;
};

class Solution {
public:
    int findCircleNum(std::vector<std::vector<int>>& isConnected)
    {
        DisjointSet ds(isConnected.size());
        std::set<int> provinces;

        for(int j = 0; j < isConnected.size(); j++)
        {
            for(int i = j ; i < isConnected[j].size(); i++)
            {
                if(isConnected[j][i] == 1)
                {
                    ds.Union(j, i);
                }
            }
        }
        
        for(int i = 0; i < isConnected.size(); i++)
        {
            provinces.insert(ds.Find(i));
        }
        
        return provinces.size();
    }
};

