// 456. 132 Pattern (1/6/54320)
// Runtime: 69 ms (93.43%) Memory: 37.95 MB (94.30%) 

#include <climits>
class Solution {
public:
bool find132pattern(std::vector<int>& nums) {
        int s3 = INT_MIN;
        std::vector<int> st;
        for( int i = nums.size()-1; i >= 0; i -- ){
            if( nums[i] < s3 )
            {
                return true;
            }
            else {
                while (!st.empty() && nums[i] > st.back()) {
                    s3 = st.back();
                    st.pop_back();
                }
            }
            st.push_back(nums[i]);
        }
        return false;
    }
};