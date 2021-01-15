# https://www.codewars.com/kata/56882731514ec3ec3d000009/train/python

COLUMNS, ROWS = 'ABCDEFG', range(6)
LINES = [{(COLUMNS[i+k], ROWS[j]) for k in range(4)}
           for i in range(len(COLUMNS) - 3) for j in range(len(ROWS))] \
        + [{(COLUMNS[i], ROWS[j+k]) for k in range(4)}
           for i in range(len(COLUMNS)) for j in range(len(ROWS) - 3)] \
        + [{(COLUMNS[i+k], ROWS[j+k]) for k in range(4)}
           for i in range(len(COLUMNS) - 3) for j in range(len(ROWS) - 3)] \
        + [{(COLUMNS[i+k], ROWS[j-k]) for k in range(4)}
           for i in range(len(COLUMNS) - 3) for j in range(3, len(ROWS))]

def who_is_winner(pieces_positions):
    players = {}
    board = dict.fromkeys(COLUMNS, 0)
    for position in pieces_positions:
        column, player = position.split('_')
        pos = (column, board[column])
        board[column] += 1
        players.setdefault(player, set()).add(pos)
        if any(line <= players[player] for line in LINES):
            return player
    return "Draw"




# test
who_is_winner([ 
  "C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red", "B_Yellow", "G_Red", "C_Yellow", "C_Red",
  "D_Yellow", "F_Red", "E_Yellow", "A_Red", "A_Yellow", "G_Red", "A_Yellow", "F_Red", "F_Yellow", "D_Red", 
  "B_Yellow", "E_Red", "D_Yellow", "A_Red", "G_Yellow", "D_Red", "D_Yellow", "C_Red"
])



# if __name__ == "__main__":
