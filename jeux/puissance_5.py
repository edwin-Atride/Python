# Premier programme
ROWS = 6
COLUMNS = 7

def create_board():
    return [[" " for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    print("\n  " + "   ".join(str(i+1) for i in range(COLUMNS)))
    print(" +" + "---+" * COLUMNS)
    for row in board:
        print(" | " + " | ".join(row) + " |")
        print(" +" + "---+" * COLUMNS)

def is_valid_location(board, col):
    return board[0][col] == " "

def get_next_open_row(board, col):
    for r in range(ROWS-1, -1, -1):
        if board[r][col] == " ":
            return r
    return -1

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def winning_move(board, piece):
    # Vérification horizontale
    for r in range(ROWS):
        for c in range(COLUMNS - 3):
            if all(board[r][c+i] == piece for i in range(4)):
                return True

    # Vérification verticale
    for r in range(ROWS - 3):
        for c in range(COLUMNS):
            if all(board[r+i][c] == piece for i in range(4)):
                return True

    # Vérification diagonale /
    for r in range(3, ROWS):
        for c in range(COLUMNS - 3):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True

    # Vérification diagonale \
    for r in range(ROWS - 3):
        for c in range(COLUMNS - 3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True

    return False

def is_board_full(board):
    return all(board[0][c] != " " for c in range(COLUMNS))

def main():
    board = create_board()
    game_over = False
    turn = 0

    print("\nBienvenue dans le jeu Puissance 4 !")
    print_board(board)

    while not game_over:
        piece = "X" if turn % 2 == 0 else "O"
        try:
            col = int(input(f"Joueur {1 if piece == 'X' else 2} ({piece}), choisissez une colonne (1-{COLUMNS}): ")) - 1
            if col < 0 or col >= COLUMNS:
                print("Colonne invalide. Réessayez.")
                continue
        except ValueError:
            print("Entrée invalide. Entrez un numéro de colonne.")
            continue

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, piece)

            print_board(board)

            if winning_move(board, piece):
                print(f"🎉 Joueur {1 if piece == 'X' else 2} ({piece}) a gagné !")
                game_over = True
            elif is_board_full(board):
                print("Match nul ! Le plateau est plein.")
                game_over = True
            else:
                turn += 1
        else:
            print("Cette colonne est pleine. Choisissez une autre.")

if __name__ == "__main__":
    main()
