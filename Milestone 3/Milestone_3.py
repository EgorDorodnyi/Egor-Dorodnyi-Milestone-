#storing anser and questions
#if bum == Right_answer[0]:
def Run_quiz():
    score = 0
    Right_answer = ["A", "D", "C", "B", "A"]
    Questions = ["what does Italy make the most of?", "what contory has the oldest University?", "when was  University of Bologna founded",
              "what did Itay event?", "how old is the Roman Colosseum?"]

    print("welcome to my Italy quiz\nInput A, B, C, D for it to regster as the right answer!")


    #questions
    answer1 = input(" {}\nA: Wine\nB: Chezz\nC: pasta\nD: mac and chezz\n:".format(Questions[0])).upper()

    if answer1 == Right_answer[0]:
        print("you got it right, Good boyyyyy :)")
        score += 1
    else:
        print(" Thats wrong!\n Italy is the largist producer of wine in the World")


    answer2 = input(" {}\nA: Brazil\nB: Usa\nC: UK\nD: Italy\n:".format(Questions[1])).upper()

    if answer2 == Right_answer[1]:
        print("Amazing, you got it right!")
        score += 1
    else:
        print(' Thats wrong!\n Italy has the oldest University called "University of Bologna"')


    answer3 = input(" {}\nA: 839\nB: 1753\nC: 1088\nD: 1811\n:".format(Questions[2])).upper()


    if answer3 == Right_answer[2]:
        print("Your about to melt this quiz! Good job!!!!!")
        score += 1
    else:
        print(" Thats wrong!\n University of Bologna was founded in 1088")


    answer4 = input(" {}\nA: fish and chips\nB: Eyeglasses\nC: tank\nD: Computer\n:".format(Questions[3])).upper()

    if answer4 == Right_answer[3]:
        print("Your knowlage is out of this world!!")
        score += 1
    else:
        print(" Thats wrong!\n Italy invented the eyeglasses!")


    answer5 = input(" {}\nA: 2000\nB: 500\nC: 1342\nD: 6969\n:".format(Questions[4])).upper()

    if answer5 == Right_answer[4]:
        print("Thats right!! Your on fire!")
        score += 1
    else:
        print(" Thats wrong!\n The Roaman colosseum was made 2000 years ago!")


    #Prosesos if the user got all right, most right or barly any right
    if score == 5:
        print("Wow you got 5/5 questions right, Your super smart!")
        print("Thanks for playing!")
        return score
    elif score >= 3:
        print("you got {}/5! Thats a lot but, there is room for improvment.".format(score))
    elif score <= 2:
        print("you got {}/5. There could be room for improvment!\nI know you can do better!".format(score))
    
    return score

while True:
    final_score = Run_quiz()
    if final_score == 5:
        break
    try_again = input("Do you want to try again? (Y/N): ").upper()
    if try_again != "Y":
        print("Thanks for playing!")
        break










