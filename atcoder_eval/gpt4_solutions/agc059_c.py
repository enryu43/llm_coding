MOD = 10 ** 9 + 7

def count_permutations(N, pairs):
    dp = [0] * (N + 1)
    dp[0] = 1
    pair_positions = [0] * N

    for i, (A, B) in enumerate(pairs):
        pair_positions[A - 1] = max(pair_positions[A - 1], i)
        pair_positions[B - 1] = max(pair_positions[B - 1], i)

    for i in range(N):
        for j in range(i + 1, N):
            if pair_positions[j] > pair_positions[i]:
                dp[j] += dp[i]
                dp[j] %= MOD

    return dp[N - 1]

def main():
    N = int(input())
    pairs = [tuple(map(int, input().split())) for _ in range(N * (N - 1) // 2)]

    result = count_permutations(N, pairs)
    print(result)

if __name__ == "__main__":
    main()
