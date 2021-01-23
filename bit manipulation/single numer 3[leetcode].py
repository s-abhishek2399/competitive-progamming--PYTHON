class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        data=Counter(nums)
        l=[]
        for key,value in data.items():
            if(value==1):
                l.append(key)
        return l        
                
        