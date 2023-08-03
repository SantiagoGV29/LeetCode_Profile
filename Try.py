def calculate_possible_sums(arr):
    n = len(arr)
    half_n = n // 2

    # Initialize a 2D array to store the possible sum values
    dp = [[False] * (half_n * max(arr) + 1) for _ in range(half_n + 1)]

    # Base case: When no elements are selected, the sum is 0
    for i in range(half_n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(min(i, half_n), 0, -1):
            for k in range(1, half_n * max(arr) + 1):
                if k >= arr[i - 1]:
                    dp[j][k] = dp[j][k] or dp[j - 1][k - arr[i - 1]]

    return dp

def main():
    # Assuming arr is the input array
    arr = [1, 2, 9, 4, 5, 6]

    # Calculate the possible sums for the first half
    first_half_sums = calculate_possible_sums(arr[:len(arr) // 2])

    # Calculate the possible sums for the second half
    second_half_sums = calculate_possible_sums(arr[len(arr) // 2:])

    # Example usage: Print the possible sums for the first half with k elements
    for k in range(len(first_half_sums)):
        print(f"Possible sums for selecting {k} elements from the first half: { [i for i, val in enumerate(first_half_sums[k]) if val] }")

    # Example usage: Print the possible sums for the second half with k elements
    for k in range(len(second_half_sums)):
        print(f"Possible sums for selecting {k} elements from the second half: { [i for i, val in enumerate(second_half_sums[k]) if val] }")

if __name__ == "__main__":
    main()
