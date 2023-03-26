from collections import defaultdict
from sys import stdin

def main():
    N = int(input())
    tree = [tuple(map(int, input().split())) for _ in range(N - 1)]

    adj = defaultdict(list)
    for u, v, w in tree:
        adj[u].append((v, w))
        adj[v].append((u, w))

    def dfs(u, dist_u):
        dist[u] = dist_u
        for v, w in adj[u]:
            if dist[v] is None:
                dfs(v, dist_u ^ w)

    dist = [None] * (N + 1)
    dfs(1, 0)

    Q = int(input())
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            i, w = query[1], query[2]
            u, v, w_old = tree[i - 1]
            w_diff = w ^ w_old
            tree[i - 1] = (u, v, w)
            dist[v] ^= w_diff
        else:
            u, v = query[1], query[2]
            print(dist[u] ^ dist[v])

if __name__ == '__main__':
    main()
