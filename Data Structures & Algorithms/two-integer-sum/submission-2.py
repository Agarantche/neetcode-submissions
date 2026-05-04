class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #this set will hold numbers and their index
        seen = {}

        #want to loop through nums and add them to seen if they're not in seen and record their index
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i