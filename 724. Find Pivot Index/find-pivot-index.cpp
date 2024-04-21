// 724. Find Pivot Index (2/7/54224)
// Runtime: 48 ms (9.56%) Memory: 31.11 MB (92.77%) 

class Solution {
public:
    int pivotIndex(vector<int>& A) 
    {
        int sum = 0, left = 0, ret = -1;

        for(unsigned int i = 1; i < A.size(); i++)
        {
            sum += A[i];
        }

        for(int i = 0; i < A.size(); i++)
        {
            left += (i-1>=0) ? A[i-1] : 0;
            sum -= (i-1>=0) ? A[i] : 0;
            if(left == sum)
            {
                ret = i;
                break;
            }
        }
        return ret;
        
    }
};