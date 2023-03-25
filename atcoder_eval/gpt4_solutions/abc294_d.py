from collections import deque

def main():
    N, Q = map(int, input().split())
    events = [list(map(int, input().split())) for _ in range(Q)]

    called = deque()
    visited = set()
    for event in events:
        if event[0] == 1:
            while called and called[0] in visited:
                called.popleft()
            if len(called) < N:
                called.append(len(called) + 1)
        elif event[0] == 2:
            visited.add(event[1])
        elif event[0] == 3:
            while called[0] in visited:
                called.popleft()
            print(called[0])
            visited.add(called[0])

if __name__ == "__main__":
    main()
