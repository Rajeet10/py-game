#win=10
import random
win=random.randint(1,100)
x=int(input("enter no between 1 to 100"))
guess=1
game_over=False
while not game_over:
    if x==win:
        print(f"you win you guessed {guess} times")
        game_over=True
    else:
        if x<win:
            print("too low")
            guess+=1
            x=int(input("enter no between 1 to 100 again"))
        else:
            print("too high")
            guess+=1
            x=int(input("enter no between 1 to 100 again"))