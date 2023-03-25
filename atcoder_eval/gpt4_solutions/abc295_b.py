def explode_board(R, C, board):
    def in_range(r, c):
        return 0 <= r < R and 0 <= c < C

    def explode(r, c, power):
        for dr in range(-power, power + 1):
            for dc in range(-power, power + 1):
                if abs(dr) + abs(dc) <= power and in_range(r + dr, c + dc):
                    result[r + dr][c + dc] = "."

    result = [list(row) for row in board]

    for r in range(R):
        for c in range(C):
            if board[r][c].isdigit():
                power = int(board[r][c])
                explode(r, c, power)

    return ["".join(row) for row in result]

def main():
    R, C = map(int, input().split())
    board = [input() for _ in range(R)]

    result = explode_board(R, C, board)

    for row in result:
        print(row)

if __name__ == "__main__":
    main()
