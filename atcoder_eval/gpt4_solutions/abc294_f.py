def main():
    N, M, K = map(int, input().split())
    takahashi = [tuple(map(int, input().split())) for _ in range(N)]
    aoki = [tuple(map(int, input().split())) for _ in range(M)]

    concentrations = []

    for a, b in takahashi:
        for c, d in aoki:
            concentration = 100 * (a + c) / (a + b + c + d)
            concentrations.append(concentration)

    concentrations.sort(reverse=True)

    kth_highest_concentration = concentrations[K - 1]

    print(kth_highest_concentration)

if __name__ == "__main__":
    main()
