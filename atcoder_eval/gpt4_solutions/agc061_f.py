from math import gcd

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def perfect_strings(N, M):
    MOD = 998244353
    if gcd(N, M) != 1:
        return 0
    lcm_N_M = lcm(N, M)
    pow_2_N_M = pow(2, lcm_N_M, MOD)
    pow_2_N = pow(2, N, MOD)
    pow_2_M = pow(2, M, MOD)
    result = (pow_2_N_M - pow_2_N - pow_2_M + 2) % MOD
    return result

def main():
    N, M = map(int, input().strip().split())
    solution = perfect_strings(N, M)
    print(solution)

if __name__ == "__main__":
    main()
