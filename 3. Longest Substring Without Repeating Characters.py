class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
            
        ### sol1, two pointers actually!
        i, j, end, max_len = 0, 0, len(s)-1, -1
        while j <= end:
            if s[j] not in s[i:j]:
                j += 1
                max_len = max(max_len, j-i)
            else:
                i +=1
        return max_len
        
            
            