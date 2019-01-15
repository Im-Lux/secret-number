secret = 8

guess = int(raw_input("Pick a number from 1 to 10: "))

if guess == secret:
    print "Congratulations! You guessed the number! IT'S NUMBER 8!"
elif guess >= 11:
    print "Be sure not to choose number bigger than 10!"
elif guess <= 0:
    print "Be sure not to choose number smaller than 0!"
else:
    print "I'm sorry, but you missed. It's not number " + str(guess) + "!"