// 11. Container With Most Water (2/11/54230)
// Runtime: 154 ms (0.00%) Memory: 59.09 MB (94.54%) 

class Solution {
public:
    int maxArea(std::vector<int>& height)
    {
        int area = 0, left = 0, right = 0, h =0, w =0;
        int i = 0, j=height.size()-1;
        while(i < j)
        {
            left = height[i];
            right = height[j];
            w = j-i;
            h = std::min(left, right);
            area = std::max(area, h*w);
            if(right > left)
                i++;
            else
                j--;
        }

        return area;
    }
};