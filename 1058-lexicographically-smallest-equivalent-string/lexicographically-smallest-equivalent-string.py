import bisect

class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        d = {}
        for k, v in zip(s1, s2):
            d.setdefault(k, []).append(v)
            d.setdefault(v, []).append(k)

        cache = {}

        result = ''
        for c in baseStr:
            cached = cache.get(c)
            if not cached:
                idx = 0
                length = 1
                group = [c]
                while idx < length:
                    subgroup = d.get(group[idx], [])
                    for x in subgroup:
                        if x not in group:
                            group.append(x)
                            length += 1
                    idx += 1
                group.sort()
                for x in group:
                    cache[x] = group[0]
            result += cache.get(c)
        return result