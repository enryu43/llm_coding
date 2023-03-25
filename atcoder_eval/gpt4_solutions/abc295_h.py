def main():
    MOD = 998244353

    N, M = map(int, input().split())
    grid = [input() for _ in range(N)]

    # Precompute the number of valid states for each row and column
    valid_row = [0] * (1 << M)
    valid_col = [0] * (1 << N)

    for s in range(1 << M):
        valid = True
        for i in range(M - 1):
            if (s >> i) & 3 == 3:
                valid = False
                break
        valid_row[s] = valid

    for s in range(1 << N):
        valid = True
        for i in range(N - 1):
            if (s >> i) & 3 == 3:
                valid = False
                break
        valid_col[s] = valid

    # DP to count the number of valid grids
    dp = [[0] * (1 << M) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(N):
        for mask in range(1 << M):
            if not valid_row[mask]:
                continue
            for new_mask in range(1 << M):
                if not valid_col[new_mask]:
                    continue
                if any(((mask >> j) & 1) and ((new_mask >> j) & 1) for j in range(M)):
                    continue
                if any(grid[i][j] == '0' and ((mask >> j) & 1) for j in range(M)):
                    continue
                if any(grid[i][j] == '1' and not ((mask >> j) & 1) for j in range(M)):
                    continue
                dp[i + 1][mask] += dp[i][new_mask]
                dp[i + 1][mask] %= MOD

    print(dp[N][0])

if __name__ == "__main__":
    main()
