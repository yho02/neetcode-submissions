class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r-l) // 2
            print(mid)
            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid]: #half left is sorted
                if nums[l] <= target < nums[mid]: # target inside
                    r = mid -1
                else: # target not inside
                    l = mid + 1
            else: #half left not sorted? half right is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid +1 
                else:
                    r = mid - 1
        return -1 