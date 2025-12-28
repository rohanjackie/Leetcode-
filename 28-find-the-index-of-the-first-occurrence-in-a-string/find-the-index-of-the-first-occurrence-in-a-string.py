class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1


        #First we calculate range so haystack doesn not go out of bound for needle
        # then we check two two character each to see where needle would fit in
        