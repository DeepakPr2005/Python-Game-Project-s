import random

words = ["UMBRELLA","COMPUTER","TELESCOPE","SMARTPHONE"]
word = random.choice(words)
print(word)


total_chances = 7
gussed_word = "-"*len(word)


while total_chances !=0:
    # print(gussed_word)
    letter =input("enter the letter--->: ").upper()
    if letter in word:
        for index in range(len(word)):
            if word[index]==letter: 
                gussed_word = gussed_word[:index]+letter+gussed_word[index+1:]
                print(gussed_word)
        if gussed_word == word:
                print("Congratulations you won!!!")
                break
    else:
        total_chances-=1
        print("incorrect guess")
        print("the remaining chances are:",total_chances)
        print("you lost")
        


# print("Game over")
# print("all chances are completed")
# print("the correct word is ",word)

#https://youtu.be/SOa9lUIcIZc