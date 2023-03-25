def max_consecutive_ys(n, k, s):
    x_count, y_count = 0, 0
    for c in s:
        if c == 'X':
            x_count += 1
        else:
            y_count += 1

    y_pairs = [0] * (n + 1)
    y_pairs[0] = y_count * (y_count - 1) // 2
    y_pairs[1] = x_count * (x_count - 1) // 2 + y_count * (y_count + 1) // 2

    for i in range(2, n + 1):
        y_pairs[i] = y_pairs[i - 1] + x_count - (y_count - 1) * (y_count != 1)

    return min(y_pairs[k], y_pairs[n - k])


def main():
    n, k = map(int, input().split())
    s = input().strip()
    solution = max_consecutive_ys(n, k, s)
    print(solution)


if __name__ == "__main__":
    main()
