class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if the lengths of the two strings are not the same return false
        if len(s) != len(t):
            return False
        
        #Go through s and get char and count of chare and save in in dict count where key is letter and count of char is value
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1

        #Go Through t and see if chars from t are in s and how many times they show up
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
        
        return True
        