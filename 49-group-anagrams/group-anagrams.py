class Solution:
    def groupAnagrams(self, strs):
        groups = {}

        for word in strs:
            key = ''.join(sorted(word))   # sorted anagram signature
            if key not in groups:
                groups[key] = []
            groups[key].append(word)

        return list(groups.values())
