class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        current_prod = 1
        left_arr = [1]
        right_arr = [1] * len(nums)

        for index in range(1,len(nums)):
            current_prod = current_prod * nums[index-1]
            left_arr.append(current_prod)
        current_prod = 1
        index = len(nums) - 2
        for index in range(len(nums)-2, -1, -1):
            current_prod= current_prod * nums[index+1]
            left_arr[index] = current_prod * left_arr[index]
            index -= 1
        return left_arr


