// 1491. Average Salary Excluding the Minimum and Maximum Salary (5/21/55301)
// Runtime: 4 ms (0.00%) Memory: 7.12 MB (73.93%) 

class Solution {
public:
    double average(vector<int>& salary) {
        double average = 0;
        if(salary.empty()) return average;

        std::sort(salary.begin(), salary.end());
        int i = 0;
        for(; i < salary.size(); i++)
        {
            std::cout << salary[i] << std::endl;
            if((i == 0) || (i == salary.size()-1))
                continue;
            average += salary[i];
        }
        average /= i-2;

        return average;
    }
};