class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = len(position) 
        stack = []
        pos_spd = []
        for pos, spd in zip(position, speed):
            pos_spd.append((pos,spd))

        pos_spd = sorted(pos_spd, reverse=True)

        # a car belong to a fleet if it catches the car ahead of it before reaching destination
        # target = 10, position = [4,1,0,7], speed = [2,2,1,1]
        # [(4,6,8,10), (1,3,5,7,9,11), (0,1,2,3,4,5,6,7,8,9,10), (7,8,9,10)]
        # so at any step, if two car in the same position, become a fleet
        
        for i in range(len(position)):
            time = (target - pos_spd[i][0]) / pos_spd[i][1]
            if stack and stack[-1] >= time:
                res -= 1
            if not stack or stack[-1] < time:
                stack.append(time)  
        return res
            