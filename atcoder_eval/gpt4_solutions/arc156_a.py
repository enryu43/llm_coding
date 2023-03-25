def min_operations_to_show_tails(N, S):
    count = 0
    i = 0
    while i < N:
        if S[i] == '1':
            count += 1
            i += 2
        else:
            i += 1
    if count == N // 2:
        return count
    return -1

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input()
        solution = min_operations_to_show_tails(N, S)
        print(solution)

if __name__ == "__main__":
    main()
