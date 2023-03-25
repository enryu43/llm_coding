MOD = 998244353
inv = lambda x: pow(x, MOD - 2, MOD)

def expected_value(N, M, K, A):
    zero_count = A.count(0)
    A = [a for a in A if a > 0]
    A.sort()

    if zero_count == 0:
        return A[K - 1] % MOD

    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i % MOD

    inv_fact = [1] * (N + 1)
    inv_fact[N] = inv(fact[N])
    for i in range(N - 1, -1, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

    res = 0
    m_inv = inv(M)

    for i, a in enumerate(A):
        if i >= K - 1:
            res += a * fact[zero_count - 1 + i - (K - 1)] * inv_fact[zero_count - 1] * inv_fact[i - (K - 1)] % MOD
            res %= MOD

    res = res * pow(M, zero_count - 1, MOD) % MOD
    return res

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))

    result = expected_value(N, M, K, A)
    print(result)

if __name__ == "__main__":
    main()
