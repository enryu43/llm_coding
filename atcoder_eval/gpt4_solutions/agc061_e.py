from itertools import product

def smallest_cost(N, S, T, A, operations):
    INF = 10**18
    ans = INF
    for p in product(range(2), repeat=N):
        xor = S
        cost = 0
        for i in range(N):
            if p[i]:
                xor ^= operations[i][0]
                cost += operations[i][1]
        ans = min(ans, cost + A * (T - xor))
    if ans == INF:
        return -1
    return ans

def main():
    N, S, T, A = map(int, input().strip().split())
    operations = [tuple(map(int, input().strip().split())) for _ in range(N)]
    result = smallest_cost(N, S, T, A, operations)
    print(result)

if __name__ == "__main__":
    main()
