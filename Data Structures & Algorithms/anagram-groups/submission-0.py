class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for string in strs:
            key = ''.join(sorted(string))
            if key in seen:
                seen[key].append(string)
            else:
                seen[key]=[string]
        return list(seen.values())
            

        