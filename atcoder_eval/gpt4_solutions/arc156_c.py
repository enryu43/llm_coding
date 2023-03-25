from collections import defaultdict

def dfs(tree, node, parent):
    children = [child for child in tree[node] if child != parent]
    for child in children:
        dfs(tree, child, node)
    return [node] + [child for child in children]

def construct_permutation(N, edges):
    tree = defaultdict(set)
    for u, v in edges:
        tree[u].add(v)
        tree[v].add(u)

    root = max(tree, key=lambda x: len(tree[x]))
    permutation = dfs(tree, root, None)
    return permutation

def main():
    N = int(input())
    edges = [tuple(map(int, input().split())) for _ in range(N - 1)]
    permutation = construct_permutation(N, edges)
    print(*permutation)

if __name__ == "__main__":
    main()
