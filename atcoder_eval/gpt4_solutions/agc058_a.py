def main():
    N = int(input())
    P = list(map(int, input().split()))

    operations = []
    for i in range(2 * N - 1):
        for j in range(2 * N - 1):
            if (j % 2 == 0 and P[j] > P[j + 1]) or (j % 2 == 1 and P[j] < P[j + 1]):
                P[j], P[j + 1] = P[j + 1], P[j]
                operations.append(j + 1)

    print(len(operations))
    print(*operations)

if __name__ == "__main__":
    main()
