from sys import stdin

MOD = 998244353

def power_mod(x, n, mod):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = (result * x) % mod
        x = (x * x) % mod
        n //= 2
    return result

def main():
    N, M, K = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]

    adj = [[] for _ in range(N + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    ans = 0
    for x in range(1, K + 1):
        sum_a = 0
        for u in range(1, N + 1):
            prod = 1
            for v in adj[u]:
                prod = (prod * (x - 1)) % MOD
            sum_a = (sum_a + prod) % MOD
        ans = (ans + power_mod(x, N, MOD) - sum_a) % MOD

    print(ans)

if __name__ == '__main__':
    main()
