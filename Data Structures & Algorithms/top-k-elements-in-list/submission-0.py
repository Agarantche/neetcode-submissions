class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # holds num → frequency
        count = {}
        
        #want to loop through nums
        #then check if the num isnt recorded in count
        #record number
        #if number is alreadyy recorded and seen again increment the value
        #if number is not recorder add number to dictionary then set the value to 1
        #after sort dictionary by values
        #finally return the fist k items in dictionary

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        sorted_items = sorted(count.items(), key=lambda item: item[1], reverse=True)

        return [item[0] for item in sorted_items[:k]]

        