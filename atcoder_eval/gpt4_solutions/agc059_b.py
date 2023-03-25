from collections import Counter
from itertools import chain

def min_adjacent_pairs(test_cases):
    results = []
    for colors in test_cases:
        count_colors = Counter(colors)
        max_color = max(count_colors, key=count_colors.get)
        max_color_count = count_colors[max_color]
        remaining_colors = [color for color in colors if color != max_color]

        arrangement = [max_color] * max_color_count
        for idx, color in enumerate(remaining_colors):
            arrangement.insert(idx % max_color_count + idx, color)

        results.append(arrangement)
    return results

def main():
    T = int(input())
    test_cases = []
    for _ in range(T):
        N = int(input())
        colors = list(map(int, input().split()))
        test_cases.append(colors)

    results = min_adjacent_pairs(test_cases)

    for arrangement in results:
        print(*arrangement)

if __name__ == "__main__":
    main()
