# 167. Two Sum II - Input Array Is Sorted (12/16/55834)
# Runtime: 101 ms (17.86%) Memory: 17.28 MB (72.86%) 

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indexes = []
        i = 0
        j = len(numbers) - 1

        while i < j:
            diff = target - numbers[i]
            
            if numbers[j] > diff:
                j-=1
            elif numbers[j] < diff:
                i+=1
            else:
                indexes.append(i+1)
                indexes.append(j+1)
                break    
            
        return indexes