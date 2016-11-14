class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        while dividend >= divisor:
            current_div, i = divisor, 1
            while dividend >= current_div:
                dividend -= current_div
                result += i
                i <<= 1
                current_div <<= 1
        if not sign:
            result = -result
        return min(2**31-1, max(-2**31, result))

        