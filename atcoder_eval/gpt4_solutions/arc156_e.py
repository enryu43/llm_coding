MOD = 998244353

def binomial_coefficients(n):
    C = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        C[i][0] = 1
        C[i][i] = 1
        for j in range(1, i):
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD
    return C

def good_sequences(N, M, K):
    C = binomial_coefficients(N * M + 1)
    ans = 0
    for s in range(K + 1):
        cur = 0
        for j in range(N + 1):
            cur = (cur + C[s + j * (M - 1)][j] * C[N - 1][j]) % MOD
        ans = (ans + cur * C[s][N]) % MOD

    return ans

def main():
    N, M, K = map(int, input().split())
    result = good_sequences(N, M, K)
    print(result)

if __name__ == "__main__":
    main()
