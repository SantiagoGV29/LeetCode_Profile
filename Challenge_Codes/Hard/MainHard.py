import Hard, time, Nodes

def main():
    Trees = {}
    Trees[6] = [[0,1],[0,2],[2,3],[2,4],[2,5]]
    Trees[1] = []
    Trees[2] = [[1,0]]
    Expected = {}
    Expected[6] = [8,12,6,10,10,10]
    Expected[1] = [0]
    Expected[2] = [1,1]

    for i in Trees:
        start = time.perf_counter()
        Actual = Hard.Solution().sumOfDistancesInTree(i,Trees[i])
        end = time.perf_counter()
        print("First solution:")
        print("Tree: ",i," Expected: ",Expected[i]," Actual: ",Actual," Time: ",end-start)
        start = time.perf_counter()
        Actual = Hard.Solution().sumOfDistancesInTreeDisjktra(i,Trees[i])
        end = time.perf_counter()
        print("Dijsktra solution:")
        print("Tree: ",i," Expected: ",Expected[i]," Actual: ",Actual," Time: ",end-start)
        start = time.perf_counter()
        Actual = Hard.Solution().sumOfDistancesInTreeOp(i,Trees[i])
        end = time.perf_counter()
        print("Optimum solution:")
        print("Tree: ",i," Expected: ",Expected[i]," Actual: ",Actual," Time: ",end-start)
        print("")
    print("HARD TEST 10000 NODES")
    start = time.perf_counter()
    Hard.Solution().sumOfDistancesInTreeOp(Nodes.n, Nodes.edges)
    end = time.perf_counter()
    print("Optimum solution:")
    print("Tree: ",Nodes.n," Time: ",end-start)
    

main()