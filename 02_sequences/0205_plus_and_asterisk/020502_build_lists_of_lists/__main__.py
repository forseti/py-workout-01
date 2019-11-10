board = [['_'] * 3 for i in range(3)]
print(f"board: {board}")

board[1][2] = 'X'
print(f"board[1][2] = 'X': {board}")

weird_board = [['_'] * 3] * 3
print(f"weird_board: {weird_board}")

weird_board[1][2] = 'O'
print(f"weird_board[1][2] = '0': {weird_board}")

row = ['_'] * 3
other_weird_board = []
for i in range(3):
    other_weird_board.append(row)
print(f"other_weird_board: {other_weird_board}")

other_weird_board[2][0] = 'O'
print(f"other_weird_board[2][0]: {other_weird_board}")


other_board = []
for i in range(3):
    row = ['_'] * 3
    other_board.append(row)
print(f"other_board: {other_board}")

other_board[2][0] = 'X'
print(f"other_board[2][0] = 'X': {other_board}")
