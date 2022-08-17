from time import sleep
import threading

num_of_scores = 0


def user_time():
    while True:
        # asking the user if they want to add a timer
        time_user = input("Do you wish to do a challenge where you have a limited "
                          "time to answer the question?")
        # if user said yes
        if time_user == "yes" or time_user == "y":
            timer()
            break
        elif time_user == "no" or time_user == "n":
            print("Continue")
            break
        else:
            print("Please choose one of the option")


# asking the user question
def play_again():
    while True:
        yes_no = input("Do you wish to play the quiz again?")
        if yes_no == "yes" or yes_no == "y":
            print("Welcome back to the quiz")
            user_time()
            break
        elif yes_no == "no" or yes_no == "n":
            print("------------------------------")
            print("Thank you for playing the quiz")
            print("------------------------------")
            exit(0)
        else:
            print("Please answer the question")


# the dictionary for the quiz
questions = {'questions': 'What is the cause of deforestation?', 'question2':
    'Why is the forest important?',
             'question3': 'Why do deforestation happen?', 'question4':
                 'What are the aftermath of the effects',
             'question5': 'How to reduce deforestation?',
             'question6': 'Why should be care about deforestation?',
             'question7': 'How many years until forest is gone?',
             'question8': 'What will happen if there are no more trees?',
             'question9': 'What will happen to the animals in the forest if it '
                          'is destroyed?',
             'question10': 'What will be the future for the Earth if the '
                           'forest is gone?'}
answer = {'answers': 'a', 'answer2': 'c', 'answer3': 'b', 'answer4': 'e',
          'answer5': 'd', 'answer6': 'f', 'answer7': 'h', 'answer8': 'g',
          'answer9': 'i', 'answer10': 'j'}

# list of answers where the user will see the list of answers which they will
# answer them
list_of_answer = ["A = Human activity", "B = The reasons for deforestation "
                                        "are logging, agriculture, cattle "
                                        "ranching, overpopulation, "
                                        "etc.",
                  "C = The forest is a water cycle, soil, home to many animals"
                  "and the source of oxygen, water and clean water which is "
                  "what living beings need to survive. Erosion , and act as "
                  "an important buffer against climate change.",
                  "D = Plant a tree, use less paper, reuse paper or cardboard",
                  "E = The loss of trees and other vegetation can cause "
                  "climate change, desertification, soil erosion, fewer "
                  "crops, flooding, increased greenhouse gases in the "
                  "atmosphere, and a host of problems for indigenous people. ",
                  "F = They purify the air we breathe, filter the water we "
                  "drink, prevent erosion, and act as an important buffer "
                  "against climate change.",
                  "G =The absence of trees would result in significantly "
                  "HIGHER amounts of carbon dioxide in the air and LOWER "
                  "amounts of oxygen!",
                  "H = 100 years"
                  "I =  It causes habitat destruction, increased risk of "
                  "predation, reduced food availability, and much more. As a "
                  "result, some animals lose their homes, others lose food "
                  "sources – and finally, many lose their lives.",
                  "J = There would be massive extinctions of all groups of "
                  "organisms, both locally and globally"]
meaning = ["erosion is the action of surface processes that removes soil, "
           "rock, or dissolved material from one "
           "location on the Earth's crust, and then transports it to another "
           "location where it is deposited",
           "Greenhouse gases (also known as GHGs) are gases in the earth's "
           "atmosphere that trap heat. During the day, "
           "the sun shines through the atmosphere, warming the earth's "
           "surface. At night, earth's surface cools, "
           "releasing heat back into the air. But some of the heat is trapped "
           "by the greenhouse gases in the atmosphere."]

list_of_option = ['a', 'A', 'b', 'B', 'c', 'C', 'e', 'E', 'f', 'F', 'g', 'G',
                  'h', 'H', 'i', 'I']


# one of the questions where it asked the user the questions
def question_1():
    print("``````````````")
    print("@@@@@@@@@@@@@")
    # these print the list that are on the top
    print(list_of_answer)
    print(meaning)
    # this inputs the question in the dictionary with the first question
    user_question = input(questions['questions'])
    user_question = user_question.lower()
    if user_question not in list_of_option:
        print("-------------------------------")
        print("Please choose one of the option")
        return question_1()
    elif user_question == answer['answers'] or user_question == "A":
        global num_of_scores
        num_of_scores += 1
        print("********")
        print("Correct!")
    else:
        print("#########")
        print("Incorrect")
        pass


def question_2():
    print("`````````````")
    print("@@@@@@@@@@@@@")
    print(list_of_answer)
    print(meaning)
    user_question = input(questions['question2'])
    user_question = user_question.lower()
    if user_question not in list_of_option:
        print("-------------------------------")
        print("Please choose one of the option")
        return question_2()
    elif user_question == answer['answer2'] or user_question == "C":
        global num_of_scores
        num_of_scores += 1
        print("********")
        print("Correct!")
    else:
        print("#########")
        print("Incorrect")
        pass


def question_3():
    print("`````````````")
    print("@@@@@@@@@@@@@")
    print(list_of_answer)
    print(meaning)
    user_question = input(questions['question3'])
    user_question = user_question.lower()
    if user_question not in list_of_option:
        print("-------------------------------")
        print("Please choose one of the option")
        return question_3()
    elif user_question == answer['answer3'] or user_question == "D":
        global num_of_scores
        num_of_scores += 1
        print("********")
        print("Correct!")
    else:
        print("#########")
        print("Incorrect")
        pass


def question_4():
    print("`````````````")
    print("@@@@@@@@@@@@@")
    print(list_of_answer)
    print(meaning)
    user_question = input(questions['question4'])
    user_question = user_question.lower()
    if user_question not in list_of_option:
        print("-------------------------------")
        print("Please choose one of the option")
        return question_4()
    elif user_question == answer['answer4'] or user_question == "E":
        global num_of_scores
        num_of_scores += 1
        print("********")
        print("Correct!")
    else:
        print("#########")
        print("Incorrect")
        pass


def question_5():
    print("`````````````")
    print("@@@@@@@@@@@@@")
    print(list_of_answer)
    print(meaning)
    user_question = input(questions['question5'])
    user_question = user_question.lower()
    if user_question not in list_of_option:
        print("-------------------------------")
        print("Please choose one of the option")
        return question_5()
    elif user_question == answer['answer5'] or user_question == "D":
        global num_of_scores
        num_of_scores += 1
        print("********")
        print("Correct!")
    else:
        print("#########")
        print("Incorrect")
        pass


def question_6():
    print("`````````````")
    print("@@@@@@@@@@@@@")
    print(list_of_answer)
    print(meaning)
    user_question = input(questions['question6'])
    user_question = user_question.lower()
    if user_question not in list_of_option:
        print("-------------------------------")
        print("Please choose one of the option")
        return question_6()
    elif user_question == answer['answer6'] or user_question == "F":
        global num_of_scores
        num_of_scores += 1
        print("********")
        print("Correct!")
    else:
        print("#########")
        print("Incorrect")
        pass


def question_7():
    print("`````````````")
    print("@@@@@@@@@@@@@")
    print(list_of_answer)
    print(meaning)
    user_question = input(questions['question7'])
    user_question = user_question.lower()
    if user_question not in list_of_option:
        print("-------------------------------")
        print("Please choose one of the option")
        return question_7()
    elif user_question == answer['answer7'] or user_question == "H":
        global num_of_scores
        num_of_scores += 1
        print("********")
        print("Correct!")
    else:
        print("#########")
        print("Incorrect")
        pass


def question_8():
    print("`````````````")
    print("@@@@@@@@@@@@@")
    print(list_of_answer)
    print(meaning)
    user_question = input(questions['question8'])
    user_question = user_question.lower()
    if user_question not in list_of_option:
        print("-------------------------------")
        print("Please choose one of the option")
        return question_8()
    elif user_question == answer['answer8'] or user_question == "G":
        global num_of_scores
        num_of_scores += 1
        print("********")
        print("Correct!")
    else:
        print("#########")
        print("Incorrect")
        pass


def question_9():
    print("`````````````")
    print("@@@@@@@@@@@@@")
    print(list_of_answer)
    print(meaning)
    user_question = input(questions['question9'])
    user_question = user_question.lower()
    if user_question not in list_of_option:
        print("-------------------------------")
        print("Please choose one of the option")
        return question_9()
    elif user_question == answer['answer9'] or user_question == "I":
        global num_of_scores
        num_of_scores += 1
        print("********")
        print("Correct!")
    else:
        print("#########")
        print("Incorrect")
        pass


def question_10():
    print("`````````````")
    print("@@@@@@@@@@@@@")
    print(list_of_answer)
    print(meaning)
    user_question = input(questions['question10'])
    user_question = user_question.lower()
    if user_question not in list_of_option:
        print("-------------------------------")
        print("Please choose one of the option")
        return question_10()
    elif user_question == answer['answer10'] or user_question == "J":
        global num_of_scores
        num_of_scores += 1
        print("********")
        print("Correct!")
    else:
        print("#########")
        print("Incorrect")
        pass


def timer():
    def countdown():
        global my_timer
        # this is the time that they have which is 10 seconds
        my_timer = 10

        for x in range(10):
            my_timer = my_timer - 1
            sleep(1)
        print("!!!!!!!!!!!!!!!!!!!!!!!!")
        print("You have run out of time")
        print("You got {}/10".format(num_of_scores))
        print("Please enter again")

    countdown_thread = threading.Thread(target=countdown)

    countdown_thread.start()

    while my_timer > 0:

        print("You have 10 seconds to answer the question")

        for i in range(1, 10):
            str1 = f"question_{i}()"
            print(str1)

            eval(str1)  # call function
            # if my_timer hits 0, it will break the loop
        if my_timer == 0:
            break

    play_again()


user_time()
