def count_pairs(N, socks):
    color_count = {}
    for sock in socks:
        if sock in color_count:
            color_count[sock] += 1
        else:
            color_count[sock] = 1

    pairs = 0
    for count in color_count.values():
        pairs += count // 2

    return pairs

def main():
    N = int(input())
    socks = list(map(int, input().split()))

    result = count_pairs(N, socks)
    print(result)

if __name__ == "__main__":
    main()

