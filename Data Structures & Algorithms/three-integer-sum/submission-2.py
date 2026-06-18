class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # no duplicates
        # triples with sum = 0 
        # all index are distinct 
        triples = []
        first,second,third = 0, 1, len(nums) - 1
        nums_sorted = sorted(nums)
        # now we have a sorted list, we use left right pointer
        # first fixes 
        for first in range(len(nums)-1):
            if first > 0 and nums_sorted[first] == nums_sorted[first - 1]: 
                continue
            else:
                second = first + 1
                third = len(nums) - 1
                while second < third:
                    if nums_sorted[first] + nums_sorted[second] + nums_sorted[third] == 0:
                        # how do you move?
                        triples.append([nums_sorted[first], nums_sorted[second], nums_sorted[third]])
                        second += 1
                        third -= 1
                        while second < third and nums_sorted[second] == nums_sorted[second-1]:
                            second += 1

                    elif nums_sorted[first] + nums_sorted[second] + nums_sorted[third] > 0:
                        third -= 1
                    else: 
                        second += 1                
        # prevent duplicates
        return triples
