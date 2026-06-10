class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        index = 1
        current_prod = 1
        left_arr = [1]
        right_arr = [1]

        while index < len(nums):
            current_prod = current_prod * nums[index-1]
            left_arr.append(current_prod)
            index += 1
        current_prod = 1
        index = len(nums) - 2
        while index >= 0:
            current_prod= current_prod * nums[index+1]
            right_arr.insert(0,current_prod)
            index -= 1
        index = 0
        while index < len(nums):
            left_arr[index] = left_arr[index] * right_arr[index]
            index += 1
        return left_arr


