def beauty_of_substring(N, Q, S, queries):
    cnt = [[0] * (N + 1) for _ in range(3)]

    for i, c in enumerate(S):
        for j, letter in enumerate("ABC"):
            cnt[j][i + 1] = cnt[j][i] + int(c == letter)

    result = []
    for l, r in queries:
        result.append((r - l + 1) - max(cnt[j][r] - cnt[j][l] for j in range(3)))

    return result


def main():
    N, Q = map(int, input().split())
    S = input().strip()
    queries = [tuple(map(int, input().split())) for _ in range(Q)]

    result = beauty_of_substring(N, Q, S, queries)

    for ans in result:
        print(ans)


if __name__ == "__main__":
    main()
