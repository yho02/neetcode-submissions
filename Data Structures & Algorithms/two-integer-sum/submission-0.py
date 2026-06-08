class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for num1 in range(0,length-1):
            for num2 in range(num1+1,length):
                if (target == nums[num1]+nums[num2]):
                    return [num1, num2]

