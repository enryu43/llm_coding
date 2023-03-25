def can_construct_tree(N, A):
    min_count = min(A.count(1), A.count(2))
    max_count = max(A.count(3), A.count(4))

    if max_count - min_count >= 2:
        return "No"
    else:
        return "Yes"


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        print(can_construct_tree(N, A))

if __name__ == "__main__":
    main()
