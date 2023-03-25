def max_elements_set(N, A, B, C):
    set_AB = set()
    set_AC = set()

    for i in range(N):
        set_AB.add(A[i] if A[i] in set_AB else B[i])
        set_AC.add(A[i] if A[i] in set_AC else C[i])

    intersection = set_AB & set_AC
    k = len(intersection)
    elements = list(intersection)

    return k, elements

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    k, elements = max_elements_set(N, A, B, C)

    print(k)
    print(*elements)

if __name__ == "__main__":
    main()
