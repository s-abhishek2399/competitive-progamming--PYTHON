class Solution:
    def missingNumber(self, lst: List[int]) -> int:
        n=len(lst)
        ar_sum=sum(lst)
        nat_sum = (n*(n-1))/2 + n
        return int(nat_sum-ar_sum)