import random
winning_num = random.randint(1,100)                #it will always generate a new winning number b/w 1 and 100 after the gave is completed
guess = 1
num = int(input("guess a number between 1 and 100: "))
game_over = False
while True:
    if num == winning_num:
        print(f"you win, and you guessed this num in {guess} times")            
        break       #if the user has guessed the correct answer the game will be stopped
    else:
        if num < winning_num:
            print("too low")
            
        else:
            print("too high")  
        guess += 1                             #this will be applied to both the condition under else statement
        num = int(input("guess again: "))
        #DRY - don't repeat yourself
        
        