# starting screen
print("Welcome Stranger.")

#transition from starting screen to info screen
input("Press the \"Enter\" key to get started. ")
# info screen
age = int(input("Enter age: "))

def ages(age):
    if age <= 30:
     print("You're a baby! Cool, lets get started.") 
    else:
        print("Let's get started!")
ages(age)

name = str(input("What is your name? "))

print("You're probably wondering \"what the hell is this?\"", "Well", name, "this is a 10 question based game. I want to see if I know what I'm doing.")
print(" ")

question_one = str(input("What is CPU? "))
print(" ")

score = 0
def questions(question_one):
    while True:
        try:    
            for question in question_one:
                global score
                if question_one == "central processing unit":
                    print("Correct!")
                    score += 1
                    question_one = True
                    break
                else:
                    print("try again")
                    break
        except ValueError:
            print("Incorrect. Please try again. Make sure you're using all lowercase.")
            break            

questions(question_one)
print("score:", score)
