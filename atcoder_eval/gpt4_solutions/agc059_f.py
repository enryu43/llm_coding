from functools import lru_cache
MOD = 10**9 + 7

def comb(n, r, MOD=MOD):
    if n < r or r < 0: return 0
    r = min(r, n - r)
    num, den = 1, 1
    for i in range(1, r + 1):
        num = num * (n + 1 - i) % MOD
        den = den * i % MOD
    return num * pow(den, MOD - 2, MOD) % MOD

@lru_cache(None)
def f(x, y):
    if x == 1 or y == 1:
        return 1
    return (f(x - 1, y) + f(x, y - 1)) % MOD

def solve(N, pos, val):
    res = (comb(N - 1, pos - 1) * comb(N - 1, val - 1) % MOD * f(N - pos, val) % MOD * f(pos, N - val + 1) % MOD - 1) % MOD
    if pos == val:
        res = (res - comb(N - 1, pos - 1) + MOD) % MOD
    return res

def main():
    N, pos, val = map(int, input().split())
    print(solve(N, pos, val))

if __name__ == "__main__":
    main()
