// 15. 3Sum (4/25/56560)
// Runtime: 2026 ms (0.00%) Memory: 471.83 MB (0.00%) 

// [-1,0,1,2,-1,-4]
// [-4,-1,-1,0,1,2] sorted
//         i

class Solution {
public:

// T = x + y -> y = T - x
    std::vector<std::vector<int>> twoSum(const std::vector<int>& nums, const int target, int startIndex)
    {
        std::vector<std::vector<int>> operands;
        std::unordered_set<int> diffs;

        for(int i = startIndex+1; i < nums.size(); i++)
        {
            auto diff = target - nums[i];

            if (diffs.find(diff) != diffs.end())
            {
                operands.push_back({nums[startIndex], diff, nums[i]});
                while (i + 1 < nums.size() && nums[i] == nums[i + 1]) ++i;
            }
            diffs.insert(nums[i]);
        }

        return operands;
    }

    vector<vector<int>> threeSum(vector<int>& nums)
    {
        std::vector<std::vector<int>> threeSums;
        std::unordered_map<int, int> diffs;

        // the fact that the input is sorted allows us to skip duplicates
        std::sort(nums.begin(), nums.end());

        for(int i=0; i < nums.size(); i++)
        {
            // Skip the same element to avoid duplicate triplets
            if(i > 0 && (nums[i] == nums[i-1])) continue;

            const int target = -nums[i];
            const auto operands = twoSum(nums, target, i);

            if (!operands.empty())
            {
                threeSums.insert(threeSums.end(), operands.begin(), operands.end());
            }
        }

        return threeSums;
    }
};