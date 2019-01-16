#QuizKN.py - Kaylee
global grade
grade = 0

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

