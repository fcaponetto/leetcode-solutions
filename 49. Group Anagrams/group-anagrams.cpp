// 49. Group Anagrams (12/27/56553)
// Runtime: 19 ms (82.05%) Memory: 23.90 MB (67.37%) 

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) 
    {
        std::unordered_map<std::string, std::vector<std::string>> groupedAnagrams;

        for(const auto& str : strs)
        {
            auto sorted = str;
            std::sort(sorted.begin(), sorted.end());

            groupedAnagrams[sorted].push_back(str);
        }

        vector<vector<string>> ret;
        for (const auto& [_, vect] : groupedAnagrams)
        {
            ret.push_back(vect);
        }

        return ret;
    }

};