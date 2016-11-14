class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack =[]
        out = ""
        for i in s:
            if i !="]":
                stack.append(i)
            else:
                temp = ""
                while len(stack):
                    t = stack.pop()
                    if t =="[":
                        break
                    temp = t +temp
                stack.append(temp * self.getNum(stack))
        out += "".join(stack)
        return out
    def getNum(self, stack):
        num = ""
        while stack and stack[-1].isdigit():
            t = stack.pop()
            num = str(t) + num
        return int(num)
            
                    