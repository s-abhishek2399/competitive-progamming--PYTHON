class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        output=[]
        for i in range(len(nums) - 3):
            if(i>0 and (nums[i]==nums[i-1])):
                continue
            for j in range(i+1,len(nums)-2):
                if(j>i+1 and (nums[j]==nums[j-1])):
                    continue
                k=j+1
                r=len(nums)-1
                while(k<r):
                    res=nums[i]+nums[j]+nums[k]+nums[r]
                    if(res==target):
                        output.append([nums[i] , nums[j],nums[k],nums[r]])
                        while(k<r and nums[k]==nums[k+1]):
                            k+=1
                        while(k<r and nums[r]==nums[r-1]):
                            r-=1
                        k+=1
                        r-=1
                    elif(res<target):
                        k+=1
                    else:
                        r-=1
                j+=1
        return output