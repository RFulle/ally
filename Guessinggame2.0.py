#Guessinggame2.0
import random
def guessgame2():
    print("Hi, I'm a computer! What's your name?")
    username = str(input())
    print("Welcome to Guessing Game, {}! I'm going to pick a number between one and a hundred, and you have to find it!".format(username))
    num = random.randint(1, 100)
    guess = -1
    while guess != num:
        print("Let's have a guess, {}!".format(username))
        guess = int(input())
        if guess == num:
            print("WINNER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            break
        elif guess > num:
            print("Nope, it's smaller than {}.".format(guess))
        elif guess < num:
            print("Nope, it's bigger than {}.".format(guess))
guessgame2()