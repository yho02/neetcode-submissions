class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # solution 3: gemini's help
        l, r = 1, max(piles)
        min_k = max(piles)
        while l <= r:
            mid = l + ((r-l)//2)
            total_hours = 0
            for pile in piles:
                total_hours += -(-pile//mid)
            if total_hours > h:
                l = mid + 1
            elif total_hours <= h:
                if min_k > mid:
                    min_k = mid
                r = mid - 1
        return min_k
