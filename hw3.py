#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""This function visualizes the hangman depending on the wrong_count"""
def printHangman(wrong_count, word):
    if wrong_count == 0:
        print("·---------·")
        for i in range(10):
            if i == 0 or i == 1:
                print("|         |")
            else:
                print("|          ")
            
            
        
    elif wrong_count == 1:
        print("·---------·")
        for i in range(10):
            if i == 0 or i == 1:
                print("|         |")
            elif i == 2:
                print("|         O")
            else:
                print("|          ")
            
       
    elif wrong_count == 2:
        print("·---------·")
        for i in range(10):
            if i == 0 or i == 1:
                print("|         |")
            elif i == 2:
                print("|         O")
            elif i == 3:
                print("|        /|")
            else:
                print("|          ")
            
        
    elif wrong_count == 3:
        print("·---------·")
        for i in range(10):
            if i == 0 or i == 1:
                print("|         |")
            elif i == 2:
                print("|         O")
            elif i == 3:
                print('|        /|\\')# using one backslash causes SyntaxError(EOL while scanning string literal) Becuase it(\)'s a special character
            else:
                print("|          ")
            
        
    elif wrong_count == 4:
        print("·---------·")
        for i in range(10):
            if i == 0 or i == 1:
                print("|         |")
            elif i == 2:
                print("|         O")
            elif i == 3:
                print('|        /|\\')# using one backslash causes SyntaxError(EOL while scanning string literal) Becuase it(\)'s a special character
            elif i == 4:
                print('|        /')# using one backslash causes SyntaxError(EOL while scanning string literal) Becuase it(\)'s a special character
            else:
                print("|          ")
            
    
    elif wrong_count == 5:
        print("·---------·")
        for i in range(10):
            if i == 0 or i == 1:
                print("|         |")
            elif i == 2:
                print("|         O")
            elif i == 3:
                print('|        /|\\        GAME OVER!')# using one backslash causes SyntaxError(EOL while scanning string literal) Becuase it(\)'s a special character
            elif i == 4:
                print('|        / \\')# using one backslash causes SyntaxError(EOL while scanning string literal) Becuase it(\)'s a special character
            else:
                print("|          ")
            
    print(f"-----------            {word}")
        
        
def guessCheck(letter, animal, word):
    
    lst= []
    for i in range(len(animal)):
        if (animal[i] == letter):
            lst.append(i)
    
    l_o_w = list(word)
    for index in lst:
        print(index)
        l_o_w[index] = letter 
        

    word = ''.join(l_o_w)
    return word

def game():
    from random import randrange
    animal_list = ["DOG", "ELEPHANT", "GIRAFFE","HEDGEHOG"]
    random_number = randrange(4)
    animal = animal_list[random_number]
    len_animal = len(animal)
    name = input("Please enter your name to start the game..")
    print(f"Welcome {name}")
    print(f"{name}, this is an animal.")
    print("You have 4 wrong attempts.")
    word = ""
    for i in range(len_animal):
        word += "_"

    
    attempts = 5
    while attempts >= 0:
        if word == animal:
            print()
            print("------------ YOU WON! ------------")
            print()
            return
        if attempts == 5:
            printHangman(0,word)
            
        elif attempts == 4:
            printHangman(1,word)
            
        elif attempts == 3:
            printHangman(2,word)
            
        elif attempts == 2:
            printHangman(3,word)
            
        elif attempts == 1:
            printHangman(4,word)
        elif attempts == 0:
            printHangman(5,word)
            return
        
        guess = input("Please guess a letter..")
        guess = guess.upper()
        temp_word = word
        word = guessCheck(guess,animal,word)
        if word == temp_word:
            attempts = attempts - 1
    return
    
game()


# In[ ]:




