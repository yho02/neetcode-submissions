class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_spd = []
        for pos, spd in sorted(zip(position,speed), reverse = True):
            pos_spd.append((pos,spd))

        stack = []
        for pos,spd in pos_spd:
            time = (target - pos)/ spd

            if stack and time > stack[-1]:
                stack.append(time)
            if not stack:
                stack.append(time)
        return len(stack)
            