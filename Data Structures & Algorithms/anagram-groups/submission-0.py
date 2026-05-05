class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicti = {}
        for s in strs:
           new_str = sorted(s)
           result = "".join(new_str)
           if result not in dicti:
                dicti[result]=[]
           dicti[result].append(s)
        return list(dicti.values())
        