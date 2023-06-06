import random

word_list = ["ardvark", "baboon", "camel"]
word = random.choice(word_list)
hangman = []


for i in word:
    hangman += "_"


letter = input("Guess a letter for word: ")
letter = letter.lower()
    
    


for i in range(0,len(word)-1):
        
    if(letter == word[i]):
        hangman[i] = word[i]
        
                
print(hangman)
    
    
    


