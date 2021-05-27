import random

#just a design    
print(" ***************\n A Wild computer wants you to guess!! \n ***************")
# using random module to generate random in

randomnum = random.randrange(1,100)
print(randomnum)


#making a function which tells if the number is low high or equal to random numer
userinput = None
guess = 0
while(userinput != randomnum):
    userinput = int(input("Enter any number between 1 - 100:- "))
    guess += 1
    if userinput==randomnum:
        print("You won the number was correct!")
    else:
        if userinput<randomnum:
            print("Enter a larger number!:-")
        else:
            print("Enter a smaller number!:- ")
        
    
print(f"You guessed the number coorect in {guess} guesses")


with open("highscore.txt",'r') as f:
    highscore = f.read()
bestscore = int(highscore)
if guess < bestscore:
    print(f"You just high scored your highscore is {guess} guess")

with open("highscore.txt", 'w') as f:
    f.write(str(guess))











