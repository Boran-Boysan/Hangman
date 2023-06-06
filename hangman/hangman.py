import hangman_art
import hangman_words
import random

print(hangman_art.logo)
print("\n\n")
print("Welcome to hangman game.\n")
word_list = hangman_words.word_list
word = random.choice(word_list)
hangman1 = []
hangman2 = []
display =""
for i in word:
    hangman1 += "_"
    hangman2 += "_"
display = ' '.join(hangman1)

end_game = False
hp = 7
index =6

while  end_game == False:
    check = 0
    letter = input("Guess a letter: ").lower()

    for i in hangman1:
        if(i == letter):
            print("You choose it again.")

    

    for i in range(0,len(word)):
        if(word[i] == letter):
            hangman1[i] = letter
        
    
         
    print(hangman1)

    if(hangman1 == hangman2):
        hp-=1
        print(hangman_art.stages[index])
        index-=1

    else:
        for i in range(0,len(hangman1)):
            hangman2[i] = hangman1[i]
    
    if(hp <=0):
        print("You lose!")
        print("Chosen word is "+word+".")
        end_game = True

    for i in hangman1:
        if i != "_":
            check +=1

    if(check == len(word)):
        print("You win!")
        end_game = True
        

    