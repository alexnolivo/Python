import random

def number_game():
    name = input("What is your name?\n")
    print("Hello, " +name+ ", let's play a game. Pick a number between 1-10, if you guess the number correctly, you win.")
    num = random.randint(0, 10)
    usernum = int(input("Pick a number.\n")) 
    guesses = 0 

    while usernum != num:
        if usernum > num:
            guesses +=1
            print("Too high. You chose {} and the computer chose {}.\n".format(usernum, num))
            usernum = int(input("Pick another number."))
            num = random.randint(0, 10)
        elif usernum < num: 
            guesses +=1
            print("Too low. You chose {} and the computer chose {}. Try again.\n".format(usernum, num))
            usernum = int(input("Pick another number.\n"))
            num = random.randint(0, 10)
    else:
        guesses +=1
        print(f"Congratulations, "+name+f"! It took you {guesses} tries to guess correctly!")  
        
number_game()
