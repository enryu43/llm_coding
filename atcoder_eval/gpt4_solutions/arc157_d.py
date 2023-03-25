MOD = 998244353

def powmod(x, n, m):
    if n == 0:
        return 1
    res = powmod(x, n // 2, m)
    res = (res * res) % m
    if n % 2 == 1:
        res = (res * x) % m
    return res

def fence_ways(h, w, grid):
    y_count = sum(row.count('Y') for row in grid)
    if y_count % 2 != 0:
        return 0

    pow2_h = [powmod(2, i, MOD) for i in range(h + 1)]
    pow2_w = [powmod(2, i, MOD) for i in range(w + 1)]

    result = 0
    for i in range(1, h):
        for j in range(1, w):
            ways_h = (pow2_h[i - 1] - 1) * (pow2_h[h - i] - 1) % MOD
            ways_w = (pow2_w[j - 1] - 1) * (pow2_w[w - j] - 1) % MOD
            result += ways_h * ways_w % MOD
            result %= MOD

    return (result * powmod(2, y_count // 2 - 1, MOD)) % MOD

def main():
    h, w = map(int, input().split())
    grid = [input().strip() for _ in range(h)]
    solution = fence_ways(h, w, grid)
    print(solution)

if __name__ == "__main__":
    main()
