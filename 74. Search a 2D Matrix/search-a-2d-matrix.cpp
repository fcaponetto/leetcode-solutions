// 74. Search a 2D Matrix (1/4/56544)
// Runtime: 3 ms (44.17%) Memory: 12.26 MB (0.00%) 

class Solution {
public:
    bool search(const std::vector<int>& vect, int target)
    {
        int L = 0;
        int R =  vect.size() - 1;

        while (L <= R)
        {
            auto mid = (L + R) / 2;

            if (target > vect[mid])
            {
                L = mid + 1;
            }
            else if (target < vect[mid])
            {
                R = mid -1;
            }
            else
            {
                return true;
            }
        }

        return false;
    }

    bool searchMatrix(vector<vector<int>>& matrix, int target) 
    {
        // Search for the starting row by looking at the last element
        for(const auto& row : matrix)
        {
            if (target <= row[row.size()-1])
            {
                // binary search
                return search(row, target);
            }
        }

        return false;
    }
};