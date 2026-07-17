class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            p = l + ((r - l)//2)
            val = nums[p]
            if val == target:
                return p
            elif val < target:
                l = p + 1
            else:
                r = p - 1
        return -1