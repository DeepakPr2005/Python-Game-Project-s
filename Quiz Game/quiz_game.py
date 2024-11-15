questiones = ("Your name is ?",
              "Where are from ?",
              "your persuing cources is ?",
              "your class is ?",
              "your college is ?")

options = (("A. Deepak ","B. Shubham","C. Manish","D. Ganesh"),
           ("A. Kota","B. Jaipur","C. Udaipur","D. Swai-Madhopur"),
           ("A. B.Tech","B. B.Sc","C. B.Art","D. B.Com"),
           ("A. 1st-Year","B. 2nd-Year","C. 3rd-Year","D. 4rh-Year"),
           ("A. Arya college","B. Subodh college","C. Poornima college","D. JCERC college"))


answers = ("A","A","A","C","A")
gusses = []
score = 0
questiones_num = 0
  


for questione in questiones:
        print("......................")
        print(questione)
        for option in options[questiones_num]:
                print(option)


        guess = input("Enter ( A, B, C, D)".upper())
        gusses.append(guess)
        if guess == answers[questiones_num]:
                score +=1
                print("CORRECT")
        else:
               print("YOUR ANSWER IS INCORRECT")
               print(f"{answers[questiones_num]} is the correct answer")
        questiones_num +=1
        
                

print("..........................")
print("         RESULT           ")
print("..........................")

print("answers:", end= "")
for answer in answers:
        print(answer, end = "")
print()

print("gusses: ", end= "")
for guess in gusses:
        print(guess, end = "")
print()


score= (score/len(questiones)*100)
print(f"Youe score is : {score}%")

#https://youtu.be/zehwgTB0vV8