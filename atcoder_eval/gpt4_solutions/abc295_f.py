def count_substrings(S, L, R):
    def count_occurrences(S, x):
        str_x = str(x)
        return str_x.count(S)

    total_occurrences = 0
    for x in range(L, R + 1):
        total_occurrences += count_occurrences(S, x)

    return total_occurrences

def main():
    T = int(input())
    for _ in range(T):
        S, L, R = input().split()
        L, R = int(L), int(R)
        result = count_substrings(S, L, R)
        print(result)

if __name__ == "__main__":
    main()
