class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        
        """
        result = []
        pathList = path.split("/")
        for a in pathList:
            if a:
                if a == "..":
                    if result:
                        result.pop()
                elif a != "." and a !="":
                    result.append(a)
        return "/" + "/".join(result)