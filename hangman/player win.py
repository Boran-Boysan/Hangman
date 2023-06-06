import random

word_list = ["ardvark", "baboon", "camel"]
word = random.choice(word_list)

hangman = []
for i in word:
    hangman += "_"

win = 0

while win ==0:
    check = 0
    letter = input("Guess a letter: ").lower()
    for i in range(0,len(word)):
        if(word[i] == letter):
            hangman[i] = letter


    print(hangman)

    for i in hangman:
        if i != "_":
            check +=1
    if(check == len(word)):
        print("You win!")
        win = 1
    

