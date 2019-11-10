# 02_sequences/0205_plus_and_asterisk/020502_build_lists_of_lists

We can initialize a list with a certain number of 
nested lists.

A list with three lists of length 3, for tic-tac-toe:
```python
board = [['_'] * 3 for i in range(3)] # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
board[1][2] = 'X' # [['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']]
```

Another way of creating the list above:
```python
other_board = []
for i in range(3):
    row = ['_'] * 3
    other_board.append(row)

other_board[1][2] = 'X'
```

A wrong way to create the list above is by creating
a list with three references to the same list:
```python
weird_board = [['_'] * 3] * 3 # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

weird_board[1][2] = 'O' # [['_', '_', 'O'], ['_', '_', 'O'], ['_', '_', 'O']]
```

Another way of creating the wrong list above:
```python
row = ['_'] * 3
other_weird_board = []
for i in range(3):
    other_weird_board.append(row)

other_weird_board[1][2] = 'O'
```
