import bisect

class Solution(object):
    def minimumDifference(self, nums):
        Combinations = self.Create_Combinations(nums)
        better_combinations = {}
        for combination in Combinations:
            a,b = combination
            value = abs(sum(a) - sum(b))
            if value not in better_combinations:
                better_combinations[value] = combination
        return min(better_combinations.keys())


    def Create_Combinations(self,nums):
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

#Optimized

    def minimumDifferenceOP(self, nums):
        def get_combinations(arr, k):
            def generate_combinations(start, current_comb):
                if len(current_comb) == k:
                    res.append(list(current_comb))
                    return
                for i in range(start, len(arr)):
                    current_comb.append(arr[i])
                    generate_combinations(i + 1, current_comb)
                    current_comb.pop()
            res = []
            generate_combinations(0, [])
            return sorted(res,key=sum)

        N = len(nums) // 2
        ans = abs(sum(nums[:N]) - sum(nums[N:]))
        total = sum(nums)
        half = total // 2

        for k in range(1, N):
            left_combinations = get_combinations(nums[:N], k)
            right_combinations = get_combinations(nums[N:], N - k)
            right = [sum(comb) for comb in right_combinations]

            for x in left_combinations:
                r = half - sum(x)
                p = bisect.bisect_left(right, r)
                if 0 <= p < len(right):
                    left_ans_sum = sum(x) + right[p]
                    right_ans_sum = total - left_ans_sum
                    diff = abs(left_ans_sum - right_ans_sum)
                    ans = min(ans, diff)

        return ans