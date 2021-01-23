class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic=Counter(nums)
        data=max(dic.keys(),key=dic.get)
        return data
        