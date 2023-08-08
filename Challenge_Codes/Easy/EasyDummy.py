class Solution(object):
    def distinctDifferenceArray(self, nums):
        diff = []
        for i in range(len(nums)):
            pre=[]
            suff=[]
            for j in range(i+1):
                if nums[j] not in pre:
                    pre.append(nums[j])
            for j in range(i+1,len(nums)):
                if nums[j] not in suff:
                    suff.append(nums[j])
            diff.append((len(pre)-len(suff)))
        return diff