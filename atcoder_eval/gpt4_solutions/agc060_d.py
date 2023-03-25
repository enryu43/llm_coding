MOD = 998244353

def factorial_mod(n, mod=MOD):
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % mod
    return result

def pair_permutations(N):
    fact_n = factorial_mod(N)
    fact_n_1 = factorial_mod(N - 1)
    result = (fact_n * fact_n - 2 * fact_n_1 * fact_n_1) % MOD
    return result

def main():
    N = int(input().strip())
    solution = pair_permutations(N)
    print(solution)

if __name__ == "__main__":
    main()
