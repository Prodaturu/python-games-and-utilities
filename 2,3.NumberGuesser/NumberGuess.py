import random

def guess(x):
    print(f"guess the random number in {x} attempts")
    ran_num = random.randint(1,x)
    i = 20
    guess = 0
    while ((guess != ran_num) and i>=0 ):
      guess = int(input(f' Attempt {21-i}, Guess a number b/w 1 and {x}: '))
      if guess == ran_num :
        print(f'You guess {ran_num} with a score {i}!')
      elif guess < ran_num:
        print('Too Low!')
        i = i-1
      elif guess > ran_num:
        print('Too High!')
        i = i-1
      

# guess(2)
