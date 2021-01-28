class Solution(object):
    def threeSumClosest(self, nums, target):
        size=len(nums)
        minimum_difference=abs((nums[0]+nums[1]+nums[2])-target)
        best_till_now=nums[0]+nums[1]+nums[2]
        for i in range(0,size):
            for j in range(i+1,size):
                for k in range(j+1,size):
                    new_difference=abs((nums[i]+nums[j]+nums[k])-target)
                    if(new_difference < minimum_difference):
                        minimum_difference=new_difference
                        best_till_now=nums[i]+nums[j]+nums[k]
        return best_till_now
        