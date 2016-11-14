class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        out = {}
        result = ""
        for i in s:
            out[i] = out.get(i,0) +1
        out_sort = sorted(out.items(), key=lambda x:x[1],reverse=True)
        for key, val in out_sort:
            result += key * val
        return result
            