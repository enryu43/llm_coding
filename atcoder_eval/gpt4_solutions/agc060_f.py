MOD = 998244353

def number_of_spanning_trees(N, C):
    fact = [1]
    for i in range(1, N * N + 1):
        fact.append(fact[-1] * i % MOD)

    inv_fact = [1] * (N * N + 1)
    inv_fact[-1] = pow(fact[-1], MOD - 2, MOD)
    for i in range(N * N, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD

    def comb(n, r):
        if n < r or r < 0:
            return 0
        return fact[n] * inv_fact[r] * inv_fact[n - r] % MOD

    ans = 1
    for i in range(N):
        for j in range(i + 1, N):
            ans *= comb(C[i][j] + j - i - 1, C[i][j])
            ans %= MOD

    return ans

def main():
    N = int(input().strip())
    C = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        C[i] = [0] * i + C[i]

    print(number_of_spanning_trees(N, C))

if __name__ == "__main__":
    main()
