from helpers import draw_board, player_turn, check_for_win
import os

spots = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}

playing = True
complete = False
turn = 0
prev_turn = -1

while playing:
    #Reset game
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)
    #If not the players turn, let's the player know
    if prev_turn == turn:
        print("Invalid spot, please choose another.")
    prev_turn = turn
    print("Player " +str((turn % 2) +1 ) + "'s turn: Pick spot or press 'q' to quit")
    #Gathers input from player
    choice = input()
    if choice == 'q':
        playing = False
    #Check if player input is valid spot on board (1-9)
    elif str.isdigit(choice) and int(choice) in spots:
        #Check if player spot has already been taken
        if not spots[int(choice)] in {"X", "O"}:
            #Valid input, updates board
         turn += 1
         spots[int(choice)] = player_turn(turn)
    #Check if the game has ended by a player win
    if check_for_win(spots): playing, complete = False, True
    #if tie *no decalred winner
    if turn > 8: playing = False

#End of loop, print results
#Draw board final time
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)
#If game ends by player win, state who won
if complete:
  if player_turn(turn) == 'X': print("Player 1 Wins!")
  else: print("Player 2 Wins!")
else: #Tie game
  print("Draw, no winner.")

print("Thanks for playing!")