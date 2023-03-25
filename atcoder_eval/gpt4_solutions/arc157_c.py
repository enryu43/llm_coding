MOD = 998244353

def binomial_coefficient(n, k):
    if k > n - k:
        k = n - k
    res = 1
    for x in range(k):
        res = res * (n - x) // (x + 1)
    return res

def sum_of_scores(h, w, grid):
    dp = [[0] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if i == 0 and j == 0:
                dp[i][j] = 1
            else:
                if i > 0:
                    dp[i][j] += dp[i-1][j] * binomial_coefficient(i + j - 1, j)
                if j > 0:
                    dp[i][j] += dp[i][j-1] * binomial_coefficient(i + j - 1, i)
                dp[i][j] %= MOD

    result = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'Y':
                result += dp[i][j] * dp[h - i - 1][w - j - 1] % MOD * binomial_coefficient(i + j, i) % MOD
                result %= MOD

    return result

def main():
    h, w = map(int, input().split())
    grid = [input().strip() for _ in range(h)]
    solution = sum_of_scores(h, w, grid)
    print(solution)

if __name__ == "__main__":
    main()
