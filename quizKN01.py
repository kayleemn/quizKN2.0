#QuizKN.py - Kaylee

global grade
grade = 0

#defining a function
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

#question 3
q3 = """ What is Drake's real name?
1)Champagne Papi
2)Jimmy Brooks
3)Aubrey Graham
4)Joey Tamarin"""

a3 = int(0)
check3 = bool(False)
q3Ans = 3

#question 4
q4 = """ What's the name of Drake's first mixtape?
1)Room for Improvement 
2)Thank Me Later
3)So Far Gone
4)Comeback Season"""

a4 = int(0)
check4 = bool(False)
q4Ans = 1

#question 5
q5 = """ Drake played Jimmy Brooks on what teen drama show?
1)Friends
2)One Tree Hill
3)Degrassi: The Next Generation
4)Gossip Girl"""

a5 = int(0)
check5 = bool(False)
q5Ans = 3

#question 6
q6 = """In 2009, which label did Drake signed a record deal with?
1)Bad Boy Records 
2)LBW Entertainment
3)Stacks on Deck Enetertainment 
4)Young Money Entertainment"""

a6 = int(0)
check6 = bool(False)
q6Ans = 4

#question 7
q7 = """Drake's song 'Forever' features which other rap artists?
1)Kanye West, Usher, Rick Ross
2)Lil Wayne, Eminem, Kanye West
3)Nicki Minaj, Tyga, Eminem
4)Rick Ross, Trey Songz, Birdman """

a7 = int(0)
check7 = bool(False)
q7Ans = 2

#question 8
q8 = """How many songs does the 'Take Care' Album have?
1)15
2)20
3)12
4)19"""

a8 = int(0)
check8 = bool(False)
q8Ans = 4

#question 9
q9 = """Which album is Drake's song 'Fear' in?
1)So Far Gone
2)Take Care
3)Views
4)Nothing Was the Same"""

a9 = int(0)
check9 = bool(False)
q9Ans = 1

#question 10
q10 = """What's my favorite Drake song?
1)Headlines
2)Best I Ever Had
3)MIA
4)Signs"""

a10 = int(0)
check10 = bool(False)
q10Ans = 1
          
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




    

