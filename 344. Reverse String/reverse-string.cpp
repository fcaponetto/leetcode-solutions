// 344. Reverse String (1/10/54232)
// Runtime: 16 ms (61.75%) Memory: 23.22 MB (94.88%) 

class Solution {
public:
    void reverseString(vector<char>& s) {
        // vector<char> temp(s.size());
        char temp;
        
        for(unsigned int i=0, j=s.size()-1; i < s.size()/2; i++,j--)
        {
            temp = s[j];
            s[j] = s[i];
            s[i] = temp;
        }
        
        // s = temp;
    }
};