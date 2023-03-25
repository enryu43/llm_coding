def find_xor(N, K, A):
    xor_result = 0
    for i in range(N):
        for j in range(i + 1, N):
            xor_result ^= (A[i] + A[j]) * (K % 2)

    return xor_result

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    result = find_xor(N, K, A)
    print(result)

if __name__ == "__main__":
    main()
