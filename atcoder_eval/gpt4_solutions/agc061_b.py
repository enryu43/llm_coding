def is_suitable_coloring_possible(N):
    if N % 2 == 0:
        return False
    return True

def suitable_coloring(N):
    coloring = [[0] * (N + 1) for _ in range(N)]

    for i in range(N):
        for j in range(N + 1):
            color = (i + j) % N + 1
            coloring[i][j] = color

    return coloring

def main():
    T = int(input().strip())
    for _ in range(T):
        N = int(input().strip())
        if is_suitable_coloring_possible(N):
            print("Yes")
            coloring = suitable_coloring(N)
            for row in coloring:
                print(" ".join(str(x) for x in row))
        else:
            print("No")

if __name__ == "__main__":
    main()
