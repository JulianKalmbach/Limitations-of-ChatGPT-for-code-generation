Pos = tuple[int, int]
Board = dict[Pos, str]  # Only "X", "O" and "_" are valid.


def read_board_from_file(filename: str) -> Board:
    """Return a `Board` from a simple text file which contains the current
    playing field, for example, as follows:

    XOX
    OXX
    ___
    """
    with open(filename, "r") as f:
        board = dict()

        for row, line in enumerate(f):
            for col, char in enumerate(line):
                board[(row, col)] = char if char in "XO_" else "_"

    return board


def read_board_from_str(string: str) -> Board:
    """Return a `Board` from a simple string, which contains the current
    playing field in a continous form, for example, as follows:

    XOXOXX___
    """
    assert 9 == string.count("X") + string.count("O") + string.count("_")

    board = dict()
    for row in range(3):
        for col in range(3):
            board[(row, col)] = string[row * 3 + col]

    return board


def print_board(board: Board):
    for row in range(3):
        for col in range(3):
            print(board[(row, col)], end="")
        print()


def calculate_score(board: Board, depth: int) -> int:
    """
    Return 10 if X wins, -10 if O wins or 0 if it is a draw or not
    decideable yet.
    """
    # Check rows then columns for victory.
    for i in range(3):
        if "_" != board[(i, 0)] == board[(i, 1)] == board[(i, 2)]:
            return 10 - depth if board[(i, 0)] == "X" else -10 + depth
        elif "_" != board[(0, i)] == board[(1, i)] == board[(2, i)]:
            return 10 - depth if board[(0, i)] == "X" else -10 + depth

    # Check diagonals for victory.
    if "_" != board[(0, 0)] == board[(1, 1)] == board[(2, 2)]\
            or "_" != board[(0, 2)] == board[(1, 1)] == board[(2, 0)]:
        return 10 - depth if board[(1, 1)] == "X" else -10 + depth

    # No victory for either side means a) a draw or b) not finished yet.
    return 0


def minimax(board: Board, depth: int, max_mode: bool) -> int:
    """
    Use the minimax algorithm to determine if a current game state will
    (possibly) lead to a win, a lose or a draw.
    """
    current_score = calculate_score(board, depth)

    # There is a winner.
    if current_score != 0:
        return current_score
    # If there are no moves left, return 0.
    elif "_" not in board.values():
        return 0

    # Use a working copy, so we do not alter the original `board`.
    board_copy = board.copy()
    # Use a high (low) value which can not be reached normally.
    best = -11 if max_mode else 11

    for row in range(3):
        for col in range(3):
            if board_copy[(row, col)] != "_":
                continue

            if max_mode:
                board_copy[(row, col)] = "X"
                best = max(best, minimax(board_copy, depth + 1, not max_mode))
            else:
                board_copy[(row, col)] = "O"
                best = min(best, minimax(board_copy, depth + 1, not max_mode))

            board_copy[(row, col)] = "_"

    return best


def return_best_move(board: Board) -> Pos:
    current_best = -1
    current_move = (-1, -1)
    board_copy = board.copy()

    for row in range(3):
        for col in range(3):
            if board_copy[(row, col)] != "_":
                continue

            board_copy[(row, col)] = "X"

            if minimax(board_copy, 0, False) > current_best:
                current_best = minimax(board_copy, 0, False)
                current_move = (row, col)

            board_copy[(row, col)] = "_"

    return current_move


if __name__ == "__main__":
    # board: Board = read_board_from_file("game.txt")
    board: Board = read_board_from_str("XXOOXO___")
    print(return_best_move(board))
    print(calculate_score(read_board_from_str(
        "XOX"
        "XOO"
        "XXO"), 0))
