class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list) # the output dictionary

        for s in strs:
            sorteds = ''.join(sorted(s))

            res[sorteds].append(s)

        return list(res.values())