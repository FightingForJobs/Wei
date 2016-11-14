class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators = "+-*/"
        stack = []
        for i in tokens:
            # print stack
            if i not in operators:
                stack.append(int(i))
            else:
                if i == "+":
                    a, b = stack.pop(), stack.pop()
                    stack.append(a+b)
                elif i == "-":
                    b, a = stack.pop(), stack.pop()
                    stack.append(a-b)
                elif i == "*":
                    a, b = stack.pop(), stack.pop()
                    stack.append(a*b)
                else:
                    b, a = stack.pop(), stack.pop()
                    stack.append(int(operator.truediv(a,b)))
        return stack.pop()