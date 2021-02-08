class Solution:
    def maxProfit(self, l: List[int]) -> int:
        l1=[]
        for i in range(len(l)-1):
            if(l[i+1]>l[i]):
                l1.append(l[i+1]-l[i])
        return sum(l1)      