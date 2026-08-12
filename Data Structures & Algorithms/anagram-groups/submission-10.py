class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        existingWords = {}
        for string in strs:
            sortedWord = "".join(sorted(string))
            if sortedWord not in existingWords:
                existingWords[sortedWord] = [string]
            else:
                existingWords[sortedWord].append(string)
        return list(existingWords.values())


