class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_spd = sorted(zip(position,speed), reverse = True)

        fleet_count = len(position)
        recent_time = 0 
        
        for pos,spd in pos_spd:

            time = (target- pos)/spd
            if recent_time == 0 or time > recent_time:
                recent_time = time
            elif time <= recent_time:
                fleet_count -= 1 
            
        return fleet_count 
            