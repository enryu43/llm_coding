def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    C = sorted(A + B)
    pos_A = [str(C.index(a) + 1) for a in A]
    pos_B = [str(C.index(b) + 1) for b in B]

    print(" ".join(pos_A))
    print(" ".join(pos_B))

if __name__ == "__main__":
    main()
