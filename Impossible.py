class Solution(object):
    def minimumDifference(self, nums):
        Combinations = Create_Combinations(nums)
        better_combinations = {}
        for combination in Combinations:
            a,b = combination
            value = abs(sum(a) - sum(b))
            if value not in better_combinations:
                better_combinations[value] = combination
        return min(better_combinations.keys())


def Create_Combinations(nums):
    def generate_combinations(i, a, b):
        if i == len(nums):
            if len(a) <= len(nums) // 2 and len(b) <= len(nums) // 2:
                combinations.append((a[:], b[:]))
            return

        generate_combinations(i + 1, a + [nums[i]], b)
        generate_combinations(i + 1, a, b + [nums[i]])
    combinations = []
    generate_combinations(0, [], [])
    return combinations

# Optimized


