class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        p = l + ((r - l)//2)

        while l <= r:
            print(p)
            val = nums[p]
            if val == target:
                return p
            elif val < target:
                l = p + 1
            else:
                r = p - 1
            p = l + ((r - l)//2)
        return -1