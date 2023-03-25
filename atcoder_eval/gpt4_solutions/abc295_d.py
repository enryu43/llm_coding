def count_happy_pairs(S):
    counter = [0] * 10
    for digit in S:
        counter[int(digit)] += 1

    even_digits = sum(count // 2 for count in counter)
    happy_pairs = 0

    for length in range(2, len(S) + 1, 2):
        for start in range(len(S) - length + 1):
            end = start + length // 2
            left_half = S[start:end]
            right_half = S[end:start + length]

            if sorted(left_half) == sorted(right_half):
                happy_pairs += 1
                if even_digits * 2 - length >= 2:
                    happy_pairs += even_digits * 2 - length - 1

    return happy_pairs

def main():
    S = input().strip()
    result = count_happy_pairs(S)
    print(result)

if __name__ == "__main__":
    main()
