def check_strings(N, words):
    target_words = {"and", "not", "that", "the", "you"}

    for word in words:
        if word in target_words:
            return "Yes"
    return "No"

def main():
    N = int(input())
    words = input().split()

    result = check_strings(N, words)
    print(result)

if __name__ == "__main__":
    main()
