MOD = 998244353

def main():
    N = int(input())
    P = list(map(int, input().split()))

    dp = [0] * (N + 1)
    dp[0] = 1

    for p in P:
        new_dp = [0] * (N + 1)
        for i in range(N + 1):
            if i < p:
                new_dp[i + 1] += dp[i]
                new_dp[i + 1] %= MOD
            new_dp[i] += dp[i]
            new_dp[i] %= MOD
        dp = new_dp

    ans = 0
    for i in range(1, N + 1):
        ans += dp[i] * i % MOD
        ans %= MOD

    print(ans)

if __name__ == "__main__":
    main()

