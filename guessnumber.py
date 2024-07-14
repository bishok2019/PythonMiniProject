import random

top = input("Enter a max range of number you want to guess: ")
if top.isdigit:
    top = int(top)
    if top<=0:
        print("Enter a number larger than 0.")
        quit()
else:
    print("Enter a number.")
    quit()        
r = random.randint(0, top)
# print("Random number generated is: ",r) remove comment for easy navigation
guesses = 0
while True:
    guesses+=1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    
    else :
        print("Enter a number.")
        continue

    if user_guess == r:
        print("You got it in ",guesses,"guesses!")
        break     
    elif user_guess > r:
        print("You didnot get it! You were above the number")
    else:
        print("You didnot get it! You were below the number")
        

# print("in",guesses,"guesses.")# or the below one
#print(f"you got it in {guesses} guesses.")# or the below one
#print("you got it in "+str(guesses)+" guesses.")
