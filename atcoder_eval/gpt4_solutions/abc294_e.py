def main():
    L, N1, N2 = map(int, input().split())
    row1 = [tuple(map(int, input().split())) for _ in range(N1)]
    row2 = [tuple(map(int, input().split())) for _ in range(N2)]

    ans = 0
    idx1, idx2 = 0, 0
    length1, length2 = row1[idx1][1], row2[idx2][1]
    
    while idx1 < N1 and idx2 < N2:
        if row1[idx1][0] == row2[idx2][0]:
            ans += min(length1, length2)
            if length1 < length2:
                idx1 += 1
                if idx1 < N1:
                    length1 += row1[idx1][1]
            elif length1 > length2:
                idx2 += 1
                if idx2 < N2:
                    length2 += row2[idx2][1]
            else:
                idx1 += 1
                idx2 += 1
                if idx1 < N1:
                    length1 += row1[idx1][1]
                if idx2 < N2:
                    length2 += row2[idx2][1]
        else:
            if length1 < length2:
                idx1 += 1
                if idx1 < N1:
                    length1 += row1[idx1][1]
            elif length1 > length2:
                idx2 += 1
                if idx2 < N2:
                    length2 += row2[idx2][1]
            else:
                idx1 += 1
                idx2 += 1
                if idx1 < N1:
                    length1 += row1[idx1][1]
                if idx2 < N2:
                    length2 += row2[idx2][1]

    print(ans)

if __name__ == "__main__":
    main()
