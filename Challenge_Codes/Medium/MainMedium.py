import Medium, time

def main():
    Solution = Medium.Solution()
    Matrix = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    Words = ["ABCCED","SEE","ABCB"]
    ExpectedValues = [True,True,False]
    formatted_matrix = "\n".join(["\t".join(map(str, row)) for row in Matrix])
    print(formatted_matrix)
    for w in Words:
        start = time.perf_counter()
        print("Word: ", w)
        print("Expected: ", ExpectedValues[Words.index(w)])
        print("Result: ", Solution.exist(Matrix,w))
        end = time.perf_counter()
        print("Time: ", end - start, "\n")

main()

