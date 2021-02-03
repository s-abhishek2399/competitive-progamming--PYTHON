class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if(dividend>0 and divisor>0) or (dividend<0 and divisor<0):
            result=dividend//divisor
        else:
            result=-1*((-1*dividend)//divisor)
        if result>0:
            return min(result,2**31 -1)
        else:
             return max(result,-2**31)