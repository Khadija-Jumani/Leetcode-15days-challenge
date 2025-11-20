class Solution:
    def groupAnagrams(self, strs):
        groups = {}

        for word in strs:
            count = [0] * 26  # lowercase a-z
            for c in word:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)  # hashable
            if key not in groups:
                groups[key] = []
            groups[key].append(word)

        return list(groups.values())
