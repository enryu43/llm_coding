def is_good_path(T, cases):
    results = []
    for case in cases:
        N, M, K, S = case
        xor_sum = 0
        for i in range(N + M - 2):
            if S[i] == 'R':
                xor_sum ^= (i + 1)

        if xor_sum == 0:
            results.append('Yes')
        else:
            results.append('No')

    return results

def main():
    T = int(input().strip())
    cases = []
    for _ in range(T):
        N, M, K = map(int, input().strip().split())
        S = input().strip()
        cases.append((N, M, K, S))

    solutions = is_good_path(T, cases)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
