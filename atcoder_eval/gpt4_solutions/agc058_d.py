MOD = 998244353

def power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(x * x % MOD, n // 2)
    else:
        return x * power(x, n - 1) % MOD

def count_strings(A, B, C):
    fact = [1]
    for i in range(1, A + B + C + 1):
        fact.append(fact[-1] * i % MOD)

    inv_fact = [0] * (A + B + C + 1)
    inv_fact[-1] = power(fact[-1], MOD - 2)
    for i in range(A + B + C, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD

    def comb(n, r):
        if r < 0 or r > n:
            return 0
        return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

    ans = 0
    for i in range(C + 1):
        ans += comb(A + B + i - 1, A - 1) * comb(B + i - 1, B - 1) % MOD
        ans %= MOD
    return ans

def main():
    A, B, C = map(int, input().split())
    print(count_strings(A, B, C))

if __name__ == "__main__":
    main()
