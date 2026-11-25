class Solution:

    def encode(self, strs: List[str]) -> str:
        secretwords = []
        for word in strs:
            secretwords.append(str(len(word)) + "#" + word)
        return "".join(secretwords)
    def decode(self, s: str) -> List[str]:
        storedwords = []
        i = 0 

        while i < len(s):
            j = i 
            while s[j] != "#":
                j +=1 
            length = int(s[i:j])

            word = s[j + 1 : j + 1 + length]     # grab the word right after #
            storedwords.append(word)

            i = j + 1 + length                   # jump to the next word's number

        return storedwords
        