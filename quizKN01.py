#Questions.py - Kaylee

#init variables
q1 = """ Question 1: How old is Drake?
1) 29
2) 32
3) 30
4) 35
"""

a1= int(0)
check1 = bool(False)
score = int(0)

#intro
print("Welcome to my question quiz")
print("In this progrm you'll be asked one question about my favorite artist!")
print("You have 4 options to choose from")
print("Pick your best guess!")
print()
print()

#test
print(q1)

while check1 == False:
    try:
        a1 = int(input("Choose the best reponse based on your knowledge on Drake.  "))
        if a1 == 2:
            print("Okay Cool!") #correct
            score = int(score+1)
            check1 = True
        elif 0 < a1 < 5: #acceptable
            print("Okay Cool!")
            check1 = True
        else:
            print("Please enter an integer between 0-5") #unacceptable integer
    except ValueError:
        print("Um.. let's think a little harder") # non-integer
        
 #score
print("You got a ", score * 100, "%")

