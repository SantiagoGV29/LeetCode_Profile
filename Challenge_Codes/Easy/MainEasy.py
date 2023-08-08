import EasyDummy, EasyOptimized, time

def main():
    SolutionDummy = EasyDummy.Solution()
    SolutionOptimized = EasyOptimized.Solution()
    test1 = [1,2,3,4,5]
    test2 = [3,2,3,4,2,543,5,43,53,5,432,543,6,457,65,3,521,5,43,8,3,53,6,457,45,7,658,76,876,9870]

    start = time.perf_counter()
    print("Test 1 : [1,2,3,4,5]\n")
    print("Dummy Solution: ", SolutionDummy.distinctDifferenceArray(test1),end="")
    end = time.perf_counter()
    print("Time: ", end - start)
    start = time.perf_counter()
    print("Optimized Solution: ", SolutionOptimized.distinctDifferenceArray(test1),end="")
    end = time.perf_counter()
    print("Time: ", end - start, "\n")
    print("Test 2 : [3,2,3,4,2,543,5,43,53,5,432,543,6,457,65,3,521,5,43,8,3,53,6,457,45,7,658,76,876,9870]\n")
    start = time.perf_counter()
    print("Dummy Solution: ", SolutionDummy.distinctDifferenceArray(test2),end="")
    end = time.perf_counter()
    print("Time: ", end - start)
    start = time.perf_counter()
    print("Optimized Solution: ", SolutionOptimized.distinctDifferenceArray(test2),end="")
    end = time.perf_counter()
    print("Time: ", end - start)

main()
