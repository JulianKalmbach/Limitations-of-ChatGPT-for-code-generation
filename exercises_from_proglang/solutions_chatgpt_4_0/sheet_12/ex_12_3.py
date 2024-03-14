Pos = tuple[int, int]
Board = dict[Pos, str]  # Only "X", "O", and "_" are valid.

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
            for col, char in enumerate(line.strip()):
                board[(row, col)] = char if char in "XO_" else "_"

    return board

def read_board_from_str(string: str) -> Board:
    """Return a `Board` from a simple string, which contains the current
    playing field in a continuous form, for example, as follows:

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
    for row in range(3):
        if board[(row, 0)] == board[(row, 1)] == board[(row, 2)] != "_":
            return 10 - depth if board[(row, 0)] == "X" else -10 + depth
    for col in range(3):
        if board[(0, col)] == board[(1, col)] == board[(2, col)] != "_":
            return 10 - depth if board[(0, col)] == "X" else -10 + depth
    if board[(0, 0)] == board[(1, 1)] == board[(2, 2)] != "_" or board[(0, 2)] == board[(1, 1)] == board[(2, 0)] != "_":
        return 10 - depth if board[(1, 1)] == "X" else -10 + depth
    return 0

def minimax(board: Board, depth: int, max_mode: bool) -> int:
    score = calculate_score(board, depth)

    if score == 10 - depth or score == -10 + depth:
        return score

    if all(board[pos] != "_" for pos in board):
        return 0

    if max_mode:
        best_score = -float("inf")
        for pos in board:
            if board[pos] == "_":
                board[pos] = "X"
                score = minimax(board, depth + 1, False)
                board[pos] = "_"
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for pos in board:
            if board[pos] == "_":
                board[pos] = "O"
                score = minimax(board, depth + 1, True)
                board[pos] = "_"
                best_score = min(best_score, score)
        return best_score

def return_best_move(board: Board) -> Pos:
    best_move = None
    best_score = -float("inf")

    for pos in board:
        if board[pos] == "_":
            board[pos] = "X"  # Angenommen, X ist der maximierende Spieler
            move_score = minimax(board, 0, False)
            board[pos] = "_"

            if move_score > best_score:
                best_score = move_score
                best_move = pos

    return best_move

if __name__ == "__main__":
    board: Board = read_board_from_file("C:/Users/julia/PycharmProjects/Limitations-of-ChatGPT-for-code-generation/exercises_from_proglang/sample_solutions_from_technical_faculty_uni_freiburg/sheet_12/game.txt")
    print_board(board)
    print("Best move:", return_best_move(board))
