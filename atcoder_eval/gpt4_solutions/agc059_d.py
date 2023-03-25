def can_construct(N, K, B):
    A = []
    last = 0
    for i in range(N):
        if B[i] > last:
            diff = B[i] - last
            for _ in range(diff):
                last += 1
                A.append(last)
        else:
            diff = last - B[i] + 1
            A.append(A[-K + 1] + diff)
    return A

def main():
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        B = list(map(int, input().split()))

        A = can_construct(N, K, B)
        
        if len(A) == N + K - 1:
            print("YES")
            print(*A)
        else:
            print("NO")

if __name__ == "__main__":
    main()
