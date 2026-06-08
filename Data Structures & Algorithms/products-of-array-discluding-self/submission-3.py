class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # input: a list of string
        # output: a list of string, each element is the product of all elements except [current element]
        # edges: 1. there always at least 2 elements - then always * 1 to prevent 2 elments list
        #        2. ints are between -20 and 20 
        output = []

        # use index instead of num because the num itself is not used
        index = 0
        while index < len(nums):
            temp = nums.copy()
            temp[index] = 1
            product = 1
            for num in temp:
                product = product * num
            output.append(product)
            index +=1
        return output



