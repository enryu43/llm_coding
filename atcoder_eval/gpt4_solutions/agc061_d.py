def min_penalty(N, M, matrix):
    A = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(M):
            A[i + 1][j + 1] = matrix[i][j]
    A.sort(key=sum)

    X = [0] * (N + 1)
    Y = [0] * (M + 1)
    ans = float("inf")
    for d in range(1, 2 * 10**9 + 1):
        for i in range(N + 1):
            X[i] = A[i][0] // d + 1
        for j in range(M + 1):
            Y[j] = j
        cur = 0
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                cur = max(cur, abs(X[i] * Y[j] - A[i][j]))
        if ans > cur:
            ans = cur
            bestX, bestY = X[1:], Y[1:]

    return ans, bestX, bestY

def main():
    N, M = map(int, input().strip().split())
    matrix = [list(map(int, input().strip().split())) for _ in range(N)]
    D_min, X, Y = min_penalty(N, M, matrix)
    print(D_min)
    print(" ".join(str(x) for x in X))
    print(" ".join(str(y) for y in Y))

if __name__ == "__main__":
    main()

