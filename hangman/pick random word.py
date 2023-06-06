import random
hp = 5
word_list = ["ardvark", "baboon", "camel"]
word = random.choice(word_list)
c = 1
while hp > 0:
    letter = input("Guess a letter for word: ")
    letter = letter.lower()
    for i in word:
        if letter == i:
            print("Your choice is correct")
            c = 0
            break
    if c == 1:
        print("Your choice is wrong.")
        hp-=1
        
    c=1
