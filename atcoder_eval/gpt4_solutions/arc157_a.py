def main():
    N, A, B, C, D = map(int, input().split())

    for i in range(N + 1):
        if i * A + (N - 1 - i * (A + 1)) // (B + 1) * B == B + C and \
           (N - 1 - i * (A + 1)) % (B + 1) == C:
            print("Yes")
            return

    print("No")

if __name__ == "__main__":
    main()
