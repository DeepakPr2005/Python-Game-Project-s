import random
import string

print("Welcome to our Random password generator")


def dk(): # Function only can be used for multiple time generator Random password
    #easy to generator Random password without function
    lenght = int(input("Enter the lenght of password you want:")) 
    lowerD= string.ascii_lowercase
    upperD =string.ascii_uppercase
    digitD= string.digits
    symbolD=string.punctuation
    # print(lowerD)
    # print(digitD)
    # print(upperD)
    # print(symbolD) 

    combine = lowerD + upperD + digitD + symbolD
    complete = random.sample(combine,lenght)
    print(complete)  #create a list of random number
    print(random)      #As create a list of password generator

    password = "".join(complete)
    print(password)
    dk()
dk()
#https://youtu.be/gf76lZ3PPx8