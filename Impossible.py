class Solution(object):
    def minimumDifference(self, nums):        
        Combinations = Create_Combinations(nums,len(nums))
        value = float('inf')
        Total = 0
        for i in nums:
            Total += abs(i)
        print(Total,Combinations)
        for comb in Combinations:
            v = abs(sum(comb) - (Total-sum(comb)))
            if v < value:
                value = v            
        return value


def Create_Combinations(nums, n):
    def generate_combinations(i, a):
        if len(a) == n // 2:
            combinations.append(a[:])
            return
        if i == len(nums):
            return

        generate_combinations(i + 1, a + [nums[i]])
        generate_combinations(i + 1, a)

    combinations = []
    generate_combinations(0, [])
    return combinations
