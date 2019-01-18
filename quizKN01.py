#QuizKN.py - Kaylee
global grade
grade = 0

#import file          
from quizKNdata import *

#define question/answer function
    #name the function
def run_qa_loop(qStr, qCheck, ansU, ansCor):
    print(qStr)
    
    while qCheck == False:
        try:
            ansU = int(input("Choose the best reponse based on your knowledge on Drake.  "))
            if ansU == ansCor:
                print("Okay Cool!")
                global grade
                grade +=1
                qCheck = True
            elif 0 < ansU < 5:
                print("Okay Cool!")
                qCheck = True
            else:
                print("Please enter an integer between 0-5") #unacceptable integer
        except ValueError:
            print("Um.. that's not one of the choices") # non-integer

#intro
print("Welcome to my question quiz")
print("In this progrm you'll be asked one question about my favorite artist!")
print("You have 4 options to choose from")
print("Pick your best guess!")
print()
print()

#run questions
    #questions 1-5
run_qa_loop(q1, a1, check1, q1Ans)
run_qa_loop(q2, a2, check2, q2Ans)
run_qa_loop(q3, a3, check3, q3Ans)
run_qa_loop(q4, a4, check4, q4Ans)
run_qa_loop(q5, a5, check5, q5Ans)
    #questions 5-10
run_qa_loop(q6, a6, check6, q6Ans)
run_qa_loop(q7, a7, check7, q7Ans)
run_qa_loop(q8, a8, check8, q8Ans)
run_qa_loop(q9, a9, check9, q9Ans)
run_qa_loop(q10, a10, check10, q10Ans)

#score
    print("You got a ", grade * 10, "%")

    if grade == 10: #100
        print("Good job, you really know about Drake, we can be friends, 100%")
    elif grade == 9: #90
        print("You almost got a 100%, 90%")
    elif grade == 8: #80
        print("That's okay. 80%")
    elif grade == 7: #70
        print("You're average, not the best. 70%")
    elif grade == 6: #60
        print("That's not that special, 60%")
    elif grade == 5: #50
        print("You only got half of those right, 50%")
    elif grade == 4: #40
        print("Below a 50%? You do not know Drake, 40%")
    elif grade == 3: #30
        print("I mean, not the greatest but, 30%")
    elif grade == 2: #20
        print("That was the bare minimum, 20%")
    elif grade == 1: #10
        print("You probably guessed for that one question, 10%")
    elif grade == 0: #0
        print("You know nothing about Drake, kinda sad, we can't be friends, 0%")


