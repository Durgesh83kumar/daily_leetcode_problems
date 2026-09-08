class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in group:
                group[key] = []
            group[key].append(s)

        lst = []
        for value in group.values():
            lst.append(value)
        return lst