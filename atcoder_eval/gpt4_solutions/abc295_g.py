from sys import stdin

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = int(input())

    # Prepare data structures
    edges = [set() for _ in range(N + 1)]
    for i, p in enumerate(P, 2):
        edges[p].add(i)

    # Process queries
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            u, v = query[1], query[2]
            edges[u].add(v)
        else:
            x = query[1]
            reachable = {x}
            stack = [x]
            while stack:
                node = stack.pop()
                for neighbor in edges[node]:
                    if neighbor not in reachable:
                        reachable.add(neighbor)
                        stack.append(neighbor)
            print(min(reachable))

if __name__ == "__main__":
    main()
