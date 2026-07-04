class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0 
        p = 0 
        for r in range(len(prices)):
            while prices[r] - prices[l] < 0:
                l += 1
                # this is because its garuantee that there is a lower price after the l 
            else: 
                p = max(p, prices[r] - prices[l])
        print(l,r)        
        return p