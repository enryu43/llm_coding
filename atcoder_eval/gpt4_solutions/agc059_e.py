def can_color(N, S):
    if S[0] != S[N - 1] and S[N - 1] != S[2 * N - 2] and S[2 * N - 2] != S[0]:
        return True
    if S[0] != S[N - 2] and S[N - 2] != S[2 * N - 3] and S[2 * N - 3] != S[0]:
        return True
    return False

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input().strip()
        
        if can_color(N, S):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
