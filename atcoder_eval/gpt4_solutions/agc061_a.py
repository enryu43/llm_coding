def shuffle(array, L, R):
    if R == L + 1:
        array[L - 1], array[R - 1] = array[R - 1], array[L - 1]
    else:
        shuffle(array, L, R - 1)
        shuffle(array, L + 1, R)

def solve_case(N, K):
    array = list(range(1, N + 1))
    shuffle(array, 1, N)
    return array[K - 1]

def main():
    T = int(input().strip())
    for _ in range(T):
        N, K = map(int, input().strip().split())
        result = solve_case(N, K)
        print(result)

if __name__ == "__main__":
    main()
