def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    for row in A:
        S = []
        for a in row:
            if a == 0:
                S.append('.')
            else:
                S.append(chr(a + ord('A') - 1))
        print("".join(S))

if __name__ == "__main__":
    main()
