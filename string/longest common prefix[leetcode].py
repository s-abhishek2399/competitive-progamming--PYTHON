class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output=""
        if not strs:
            return ""
        if(len(strs)==1):
            return strs[0]
        strs.sort()
        for i in range(len(strs[0])):
            if(strs[0][i]==strs[-1][i]):
                output+=strs[0][i]
            else:
                break
        return output        