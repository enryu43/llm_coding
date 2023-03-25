from sys import stdin
from math import comb

MOD = 998244353

def count_orders(N, intervals):
    events = []
    for a, b in intervals:
        events.append((a, 1))
        events.append((b, -1))
    events.sort()

    ans = 1
    count = 0
    for _, t in events:
        if t == 1:
            count += 1
            ans *= count
            ans %= MOD
        else:
            count -= 1

    for i in range(1, N + 1):
        ans *= i
        ans %= MOD

    return ans

def main():
    N = int(input().strip())
    intervals = [tuple(map(int, input().strip().split())) for _ in range(N)]
    result = count_orders(N, intervals)
    print(result)

if __name__ == "__main__":
    main()
