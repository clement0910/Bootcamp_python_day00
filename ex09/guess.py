import random

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to", end='')
print("find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")
n = input(">> ")

attempt = 1
random = ramdom.randint
if n.isdigit() is True:
    if int(n) is random:
        if (int(n) is 42):
            print("The answer to the ultimate question of life, ", end='')
            print("the universe and everything is 42.")
        print("Congratulations ! You got it on the first try !")
        exit()
else:
    print("That's not a number!")
while 1:
    attempt += 1
    n = input("What's your guess between 1 and 99?\n>> ")
    if n is "exit":
        print("Goodbye !")
        exit()
    elif n.isdigit() is False:
        print("That's not a number!")
    elif int(n) < random:
        print("Too low!")
    elif int(n) > random:
        print("Too high!")
    else:
        print("Congratulation you've got it in {} times !".format(attempt))
        exit()
