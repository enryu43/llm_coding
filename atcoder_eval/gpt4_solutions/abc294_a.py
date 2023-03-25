def main():
    N = int(input())
    A = list(map(int, input().split()))

    even_numbers = [str(a) for a in A if a % 2 == 0]
    print(" ".join(even_numbers))

if __name__ == "__main__":
    main()
