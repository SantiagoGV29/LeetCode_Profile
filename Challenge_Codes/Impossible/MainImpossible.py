import Impossible,time

def main():
    tests = [[3,9,7,3],
    [-36,36],
    [2,-1,0,4,-2,-9]]
    hard_test =[7772197,4460211,-7641449,-8856364,546755,-3673029,527497,-9392076,3130315,-5309187,-4781283,5919119,3093450,1132720,6380128,-3954678,-1651499,-7944388,-3056827,1610628,7711173,6595873,302974,7656726,-2572679,0,2121026,-5743797,-8897395,-9699694]
    expected = [2,72,0]

    for i in range(len(tests)):
        start = time.perf_counter()
        Actual = Impossible.Solution().minimumDifference(tests[i])
        end = time.perf_counter()
        print("First solution:")
        print("Test: ",tests[i]," Expected: ",expected[i]," Actual: ",Actual," Time: ",end-start)
        start = time.perf_counter()
        Actual = Impossible.Solution().minimumDifferenceOP(tests[i])
        end = time.perf_counter()
        print("Optimum solution:")
        print("Test: ",tests[i]," Expected: ",expected[i]," Actual: ",Actual," Time: ",end-start)
        print("")
    print("Hard test")
    start = time.perf_counter()
    Actual = Impossible.Solution().minimumDifferenceOP(hard_test)
    end = time.perf_counter()
    print("Optimum solution:")
    print(" Time: ",end-start, " Actual: ",Actual," Expected: ",1)

main()