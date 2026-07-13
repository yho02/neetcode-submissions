class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_spd = sorted(zip(position,speed), reverse = True)
        stack = []

        for i in range(len(pos_spd)):
            time = (target - pos_spd[i][0])/ pos_spd[i][1]

            if stack and time > stack[-1]:
                stack.append(time)
            if not stack:
                stack.append(time)
        return len(stack)
            