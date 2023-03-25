def f(a):
    visited = [False] * len(a)
    cycles = 0

    for i in range(len(a)):
        if not visited[i]:
            cycles += 1
            j = i
            while not visited[j]:
                visited[j] = True
                j = a[j] - 1

    return cycles

def find_permutation(N, K, P):
    k_min = f(P)
    if K < k_min or (K - k_min) % 2 != 0:
        return "No", None

    x = [i + 1 for i in range(N)]
    for i in range(K - k_min):
        x[i], x[i + 1] = x[i + 1], x[i]

    return "Yes", x

def main():
    T = int(input().strip())
    for _ in range(T):
        N, K = map(int, input().strip().split())
        P = list(map(int, input().strip().split()))

        result, x = find_permutation(N, K, P)
        print(result)
        if x:
            print(" ".join(map(str, x)))

if __name__ == "__main__":
    main()
