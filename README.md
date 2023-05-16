# Connect 4 implementation.
The games are a two-person zero-sum game with full information. The aim of the game is to get four chips in a row, either: horizontally, vertically or diagonally. The board consists of 6 row and 7 columns. The file ‘four_in_a_row.py’ contains the code for defining the game, the board of the game is represented as a list containing lists of all columns. All the legal actions of the game and two checks to see if the game is in a terminal state (won, draw or loss) are defined. 

## main.py 
contains a game loop that receives input (get_player_input) from the player of the game. Inputs that are legal and defined by the confines of the game are accepted.

## game_node_and_game_search.py
A complete minimax algorithm, and also a definition of a game node is defined. The alogirthm implements alfa-beta pruning to play smarter

To make the AI play better an evaluation function (eval) was implemented which is used when the depth limit is reached (instead of the zero (0) value if non terminal nodes are found). As a rule of thumb when playing four in a row, positions in the middle of the board are considered more valuable than those at the edges. A tip is to count chips value more towards the center of the board. Thus the function is implementd accordingly. 

