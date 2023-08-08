class Solution(object):
    def distinctDifferenceArray(self, nums):
        diff = []
        for i in range(len(nums)):            
            pre = set(nums[:i+1])
            suff = set(nums[i+1:])
            diff.append(len(pre)-len(suff))
        return diff