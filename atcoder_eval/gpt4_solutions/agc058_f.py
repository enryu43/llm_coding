from collections import defaultdict
from functools import lru_cache
import sys

MOD = 998244353
sys.setrecursionlimit(10 ** 9)

def main():
    N = int(input())
    edges = [tuple(map(int, input().split())) for _ in range(N - 1)]

    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    @lru_cache(None)
    def f(v, p):
        ans = 1
        for u in graph[v]:
            if u != p:
                ans *= f(u, v) + 1
                ans %= MOD
        return ans

    ans = 0
    for i in range(1, N + 1):
        ans += f(i, 0)
        ans %= MOD

    inv_n = pow(N, MOD - 2, MOD)
    print(ans * inv_n % MOD)

if __name__ == "__main__":
    main()

