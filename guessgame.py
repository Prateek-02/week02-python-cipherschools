winning_num = 53
guess = 1
num = int(input("guess a number between 1 and 100: "))
game_over = False
while not game_over:
    if num == winning_num:
        print(f"you win, and you guessed this num in {guess} times") 
        game_over = True
    else:
        if num < winning_num:
            print("too low")
            guess += 1
            num = int(input("guess again: "))
        else:
            print("too high")  
            guess += 1  
            num = int(input("guess again: "))
        
        