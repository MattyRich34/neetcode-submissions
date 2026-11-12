class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictwords = {}
        for words in strs:
            key = ''.join(sorted(words))
            if key in dictwords: 
                dictwords[key].append(words)
            else: 
                dictwords[key] = [words]

        return list(dictwords.values())