// 1. Two Sum (2/9/56554)
// Runtime: 7 ms (72.72%) Memory: 14.36 MB (14.74%) 

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    {
        // key missing operand
        // value index of the missing operand
        std::unordered_map<int, int> diffs;
        std::vector<int> indeces;

        for (int i = 0; i < nums.size(); i++)
        {
            const auto diff = target - nums[i];

            if (diffs.find(diff) != diffs.end())
            {
                indeces.push_back(diffs[diff]);
                indeces.push_back(i);
                break;
            }
            else
            {
                diffs[nums[i]] = i;
            }
        }

        return indeces;
    }
};