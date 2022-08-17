# the dictionary for the quiz
import random

#  Dictionaries are used to store data values in key:value pairs
# the items that I am storing in the dictionaries are the questions
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
# these stores the answer in the key
answer = {'answers': 'a', 'answer2': 'c', 'answer3': 'b', 'answer4': 'e',
          'answer5': 'd', 'answer6': 'f', 'answer7': 'h', 'answer8': 'g',
          'answer9': 'i', 'answer10': 'j'}

# list of answers where the user will see the list of answers which they will
# answer them
list_of_answer = ["A = Human activity", "B = The reasons for deforestation are "
                                        "logging, agriculture, cattle ranching, "
                                        "overpopulation, etc.",
                  "C = The forest is a water cycle, soil, home to many animals "
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
                  " organisms, both locally and globally"]
# this is one of the list that tells the user the meaning of some words
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
# these are the options that the user uses
list_of_option = ['a', 'A', 'b', 'B', 'c', 'C', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I']

# the scores that the user starts at the beginning
num_of_scores = 0

# this randomizes the list of answers on the top, so it can confuse the used
random.shuffle(list_of_answer)


def question_1():
    # these print the list that are on the top which is the answer
    print(list_of_answer)
    print(meaning)
    # this inputs the question in the dictionary with the first question
    user_question = input(questions['questions'])
    user_question = user_question.lower()
    # if the user doesn't choose the option on the top, then it will print the options
    # and return to the question again until they choose the options
    if user_question not in list_of_option:
        print("Please choose one of the option")
        return question_1()
    elif user_question == answer['answers'] or user_question == "A":
        # global keyword allows you to modify the variable outside the current scope
        # due to the question are in def, I need to use global to add up all the scores
        global num_of_scores
        num_of_scores += 1
        print("Correct!")
    else:
        print("Incorrect")
        pass


def question_2():
    print(list_of_answer)
    print(meaning)
    user_question = input(questions['question2'])
    user_question = user_question.lower()
    if user_question not in list_of_option:
        print("Please choose one of the option")
        return question_2()
    elif user_question == answer['answer2'] or user_question == "C":
        global num_of_scores
        num_of_scores += 1
        print("Correct!")
    else:
        pass


def question_3():
    print(list_of_answer)
    print(meaning)
    user_question = input(questions['question3'])
    user_question = user_question.lower()
    if user_question not in list_of_option:
        print("Please choose one of the option")
        return question_3()
    elif user_question == answer['answer3'] or user_question == "D":
        global num_of_scores
        num_of_scores += 1
        print("Correct!")
    else:
        pass


def question_4():
    print(list_of_answer)
    print(meaning)
    user_question = input(questions['question4'])
    user_question = user_question.lower()
    if user_question not in list_of_option:
        print("Please choose one of the option")
        return question_4()
    elif user_question == answer['answer4'] or user_question == "E":
        global num_of_scores
        num_of_scores += 1
        print("Correct!")
    else:
        pass


def question_5():
    print(list_of_answer)
    print(meaning)
    user_question = input(questions['question5'])
    user_question = user_question.lower()
    if user_question not in list_of_option:
        print("Please choose one of the option")
        return question_5()
    elif user_question == answer['answer5'] or user_question == "D":
        global num_of_scores
        num_of_scores += 1
        print("Correct!")
    else:
        pass


def question_6():
    print(list_of_answer)
    print(meaning)
    user_question = input(questions['question6'])
    user_question = user_question.lower()
    if user_question not in list_of_option:
        print("Please choose one of the option")
        return question_6()
    elif user_question == answer['answer6'] or user_question == "F":
        global num_of_scores
        num_of_scores += 1
        print("Correct!")
    else:
        pass


def question_7():
    print(list_of_answer)
    print(meaning)
    user_question = input(questions['question7'])
    user_question = user_question.lower()
    if user_question not in list_of_option:
        print("Please choose one of the option")
        return question_7()
    elif user_question == answer['answer7'] or user_question == "H":
        global num_of_scores
        num_of_scores += 1
        print("Correct!")
    else:
        pass


def question_8():
    print(list_of_answer)
    print(meaning)
    user_question = input(questions['question8'])
    user_question = user_question.lower()
    if user_question not in list_of_option:
        print("Please choose one of the option")
        return question_8()
    elif user_question == answer['answer8'] or user_question == "G":
        global num_of_scores
        num_of_scores += 1
        print("Correct!")
    else:
        pass


def question_9():
    print(list_of_answer)
    print(meaning)
    user_question = input(questions['question9'])
    user_question = user_question.lower()
    if user_question not in list_of_option:
        print("Please choose one of the option")
        return question_9()
    elif user_question == answer['answer9'] or user_question == "I":
        global num_of_scores
        num_of_scores += 1
        print("Correct!")
    else:
        pass


def question_10():
    print(list_of_answer)
    print(meaning)
    user_question = input(questions['question10'])
    user_question = user_question.lower()
    if user_question not in list_of_option:
        print("Please choose one of the option")
        return question_10()
    elif user_question == answer['answer10'] or user_question == "J":
        global num_of_scores
        num_of_scores += 1
        print("Correct!")
    else:
        pass


question_1()
question_2()
question_3()
question_4()
question_5()
question_6()
question_7()
question_8()
question_9()
question_10()
print("You've got {}/10".format(num_of_scores))
