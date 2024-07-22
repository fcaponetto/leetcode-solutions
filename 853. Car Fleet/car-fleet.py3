# 853. Car Fleet (3/18/56527)
# Runtime: 661 ms (77.49%) Memory: 39.34 MB (17.03%) 

# Even though the position and speed are provided separately, it's better to combine them'
# and sort the array on starting position based.
# [(0,1),(3,3),(5,1),(8,4),(10,2)]
# 
# Starting in a reverse order, check if car at the top of the stack will eventually catch up with#
# the current one

class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        def timeToArrive(pos, vel, target=target):
            return (target - pos)/vel

        stack = []
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(key=lambda l: l[0])
        stack.append(cars[-1])
    
        if len(position) > 1:
            for car in reversed(cars[:-1]):
                if timeToArrive(car[0], car[1]) > timeToArrive(stack[-1][0], stack[-1][1]):
                    stack.append(car)

        return len(stack)