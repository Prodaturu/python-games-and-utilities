import random
def play():
  player= input("'r' for rock, 'p' for paper, 's' for scissors:")
  opponent = random.choice(['r','p','s'])

  if player == opponent:
    return "It's a tie"
  else:
    return win(player,opponent)
  
def win(player, opponent):
  if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
    return print('you win')
  else: 
    return print('you lose')

play()