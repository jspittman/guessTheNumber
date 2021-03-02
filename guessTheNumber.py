# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money

import random  

# function declartions

def welcome():
    global guess
    global the_number
    guess = 0
    the_number = random.randint(1, 100)
    print("\tWelcome to 'Guess My Number'!")
    print("\nI'm thinking of a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible.\n")

    # set the initial values
def first_guess():
    global guess # set var to global
    global tries # init tries to 1
    try:
        guess = int(input("Take a guess: "))
    except:
        print("Please enter a whole number")
    tries = 1

def while_guess():
    global guess # set var to global
    global tries # modify var tries
    while guess != the_number and tries < 10:
        # give user feedback on lower or higher
        if guess > the_number and guess != 0:
            print("Lower...")
        elif guess < the_number and guess != 0:
            print("Higher...")
        else:
            print("")
      
        # user inputs next guess  
        try:
            guess = int(input("Take a guess: "))
        except:
            print("Please enter a whole number")
        tries += 1

#congrats
def end_game():
    global text_file # modify global var text_file
    text_file = open("scoreslist.txt", "a")
    if tries <= 10 and guess == the_number:
        print("You guessed it!  The number was", the_number)
        print("And it only took you", tries, "tries!\n")
        name = input("What is your name?: ")
        score = tries
        # Assign elements to a new tuple:
        entry = (score, name)
        # append tuple to file
        text_file.write(str(entry))
        text_file.write('\n')
        # Close text file
        text_file.close()
        # display top five scores from text_list
        print("\nThe top five scores are: \n")
        text_file = open("scoreslist.txt", "r")
        # read text file
        top_five_sorted = text_file.readlines()
#       # split text file
#       top_five_sorted = top_five_sorted.split()
#       # sort text file by top five scores
        final_sort = sorted(top_five_sorted, key=lambda x: x[1], reverse=False)
        
        # display upto top five scores
        try:
            print(final_sort[0])
        except:
            pass
        try:
            print(final_sort[1])
        except:
            pass
        try:
            print(final_sort[2])
        except:
            pass
        try:
            print(final_sort[3])
        except:
            pass
        try:
            print(final_sort[4])
        except:
            pass
        
        # close open file
        text_file.close()

    else:
        print("\nSorry, you took", tries, "tries, which is too many!")
        print("\nThe number was", the_number)
        
        
#define main game loop
def main():
    global text_file
    welcome()
    first_guess()
    while_guess()
    end_game()

# main game loop
main()
