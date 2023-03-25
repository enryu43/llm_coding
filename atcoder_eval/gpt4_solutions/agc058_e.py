def check_permutation(N, A):
    stack = []
    last = 0
    for a in A:
        while stack and stack[-1] < a:
            last = stack.pop()
        if a > last + 1:
            stack.append(a - 1)
        else:
            stack.append(a)

    if stack[-1] == 1:
        return "Yes"
    else:
        return "No"

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        print(check_permutation(N, A))

if __name__ == "__main__":
    main()
