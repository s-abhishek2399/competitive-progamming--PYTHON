class Solution:
    def reverseBits(self, nums: int) -> int:
        data = "{0:032b}".format(nums)
        x=data[::-1]
        y = int(x,2)
        return y