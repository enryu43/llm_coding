MOD = 998244353

def binomial_coeff(n, k, mod=MOD):
    if k < 0 or n < k:
        return 0
    num, den = 1, 1
    for i in range(k):
        num = num * (n - i) % mod
        den = den * (i + 1) % mod
    return num * pow(den, mod - 2, mod) % mod

def heaplike_probability(N, A, B):
    n = 2 ** (N - 1)
    result = (binomial_coeff(n - 1, (2 ** A - 1)) * binomial_coeff(n - 1 - (2 ** A - 1), (2 ** B - 1) - 1)) % MOD
    return result * pow(n, MOD - 2, MOD) % MOD

def main():
    N, A, B = map(int, input().strip().split())
    solution = heaplike_probability(N, A, B)
    print(solution)

if __name__ == "__main__":
    main()

