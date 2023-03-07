# myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
# for item in myMixedTypeList:
#     print("{} is of the data type {}".format(item,type(item)))
    

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
import random
number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
    guess = int(input("Guess a number between 1 and 10: "))
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))