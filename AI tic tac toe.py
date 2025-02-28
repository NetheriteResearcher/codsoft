import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_moves_left(board):
    return any(cell == ' ' for row in board for cell in row)

def evaluate(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return 10 if row[0] == 'X' else -10
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return 10 if board[0][col] == 'X' else -10
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return 10 if board[0][0] == 'X' else -10
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return 10 if board[0][2] == 'X' else -10
    
    return 0

def minimax(board, depth, is_max, alpha, beta):
    score = evaluate(board)
    
    if score == 10 or score == -10:
        return score - depth if score == 10 else score + depth
    
    if not is_moves_left(board):
        return 0
    
    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, False, alpha, beta))
                    board[i][j] = ' '
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, True, alpha, beta))
                    board[i][j] = ' '
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = ' '
                
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
    
    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    
    print("Tic-Tac-Toe: You are 'O', AI is 'X'")
    
    while is_moves_left(board):
        print_board(board)
        row, col = map(int, input("Enter your move (row col): ").split())
        
        if board[row][col] != ' ':
            print("Invalid move. Try again.")
            continue
        
        board[row][col] = 'O'
        if evaluate(board) == -10:
            print_board(board)
            print("You win!")
            return
        
        if not is_moves_left(board):
            break
        
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = 'X'
        
        if evaluate(board) == 10:
            print_board(board)
            print("AI wins!")
            return
    
    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    main()
