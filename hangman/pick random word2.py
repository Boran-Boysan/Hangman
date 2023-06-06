import random

word_list = ["ardvark", "baboon", "camel"]
word = random.choice(word_list)
letter = input("Guess a letter for word: ")
letter = letter.lower()

for i in word:
    if(i == letter):
        print("Right!")
    else:
        print("Wrong!")
