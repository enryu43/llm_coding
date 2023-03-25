def good_string_ways(N, S):
    MOD = 998244353

    dp = [[0] * 3 for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(3):
            for k in range(3):
                if S[i] == '?' or S[i] == "abc"[j]:
                    next_j = (j + 1) % 3
                    if S[i - 1] != "abc"[next_j] or i == 0:
                        dp[i + 1][next_j] += dp[i][j]
                        dp[i + 1][next_j] %= MOD

    return sum(dp[N]) % MOD

def main():
    N = int(input().strip())
    S = input().strip()
    solution = good_string_ways(N, S)
    print(solution)

if __name__ == "__main__":
    main()
