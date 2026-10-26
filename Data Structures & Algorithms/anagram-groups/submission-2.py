class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for char in strs:
            key = "".join(sorted(char))
            if key not in group:
                group[key] = []
            group[key].append(char)
        return list(group.values())
                