from collections import Counter
MOD = 998244353

def count_multisets(N, K, A):
    counter = Counter(A)
    freq = [counter[i] for i in range(N + 1)]
    dp = [1] + [0] * (N + 1)
    
    for _ in range(K):
        for i in range(N + 1):
            dp[i + 1] = (dp[i + 1] + dp[i]) % MOD
        for i, f in enumerate(freq):
            dp[i + 1] = (dp[i + 1] - dp[i] * f) % MOD
    
    return sum(f * dp[i] for i, f in enumerate(freq)) % MOD

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    solution = count_multisets(N, K, A)
    print(solution)

if __name__ == "__main__":
    main()
