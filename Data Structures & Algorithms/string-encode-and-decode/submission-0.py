class Solution:

    #Create empty string then add words from list to string
    #To seperate i'll use the lenght of word + # + word
    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result = result + str(len(word)) + "#" + word
        return result 

    #For decoding
    # find the # then get lenght for the word and go up num characters then append word to result
    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            j = s.find("#", i)
            wordLen = int(s[i:j])
            word = s[j + 1: j + 1 + wordLen]
            result.append(word)
            i = j + 1 + wordLen
        return result
