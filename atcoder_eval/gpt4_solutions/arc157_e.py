def is_possible(N, A, B, C, parents):
    root_children = parents.count(1)
    if root_children != 2:
        return "No"

    if A > 0 and (B > 0 or C > 0):
        return "No"

    if B > 0 and C > 0:
        child_counts = [0] * (N + 1)
        for p in parents:
            child_counts[p] += 1

        if any(count != 2 and count != 0 for count in child_counts[2:]):
            return "No"

    return "Yes"

def main():
    T = int(input())
    for _ in range(T):
        N, A, B, C = map(int, input().split())
        parents = list(map(int, input().split()))
        solution = is_possible(N, A, B, C, parents)
        print(solution)

if __name__ == "__main__":
    main()
