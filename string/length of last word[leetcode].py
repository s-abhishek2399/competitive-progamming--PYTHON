class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lis=[i for i in s.split()]
        if(len(lis)==0):
             return 0
        else:
            return len(lis[-1])