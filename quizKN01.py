#QuizKN.py - Kaylee

#defining a function
    #name the function
def run_qa_loop(qStr, qCheck, ansU, ansCor):
    print(qStr)
    
    while qCheck == False:
        try:
            ansU = int(input("Choose the best reponse based on your knowledge on Drake.  "))
            if ansU == ansCor:
                print("Okay Cool!")
                #score = int(score+1)
                qCheck = True
            elif 0 < ansU < 5:
                print("Okay Cool!")
                qCheck = True
            else:
                print("Please enter an integer between 0-5") #unacceptable integer
        except ValueError:
            print("Um.. that's not one of the choices") # non-integer

#init variables
score= int(0)

#question 1
q1 = """ Question 1: How old is Drake?
1) 29
2) 32
3) 30
4) 35"""
          
a1 = int(0)
check1 = bool(False)
q1Ans = 2

#question 2
q2 = """ Question 2: When is Drake's birthday?
1) December 7th
2) July 21st
3) March 14th
4) October 24th"""
          
a2 = int(0)
check2 = bool(False)
q2Ans = 4
          
#intro
print("Welcome to my question quiz")
print("In this progrm you'll be asked one question about my favorite artist!")
print("You have 4 options to choose from")
print("Pick your best guess!")
print()
print()

#question 1
run_qa_loop(q1, a1, check1, q1Ans)
        
#question 2
run_qa_loop(q2, a2, check2, q2Ans)

#score
#print("You got a ", score * 50, "%")

