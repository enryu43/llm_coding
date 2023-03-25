def longest_common_subsequence(N, S, T):
    s_x = S.count('X')
    s_y = N - s_x
    t_x = T.count('X')
    t_y = N - t_x

    common_x = min(s_x, t_x)
    common_y = min(s_y, t_y)

    result = 'X' * common_x + 'Y' * common_y
    return result

def main():
    N = int(input())
    S = input()
    T = input()
    solution = longest_common_subsequence(N, S, T)
    print(solution)

if __name__ == "__main__":
    main()
