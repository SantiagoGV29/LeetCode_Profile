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

#Optimized


class Solution:
    def minimumDifference(self, nums):
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