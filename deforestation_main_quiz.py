import random
from time import sleep
import threading

num_of_scores = 0

list_of_random_facts = ["We Lose Around 10 Million Hectares of Forest Every "
                        "Single Year",
                        "Beef is Responsible for 41% of Global Deforestation ",
                        "Deforestation Contributes about 4.8 Billion Tonnes of"
                        " Carbon Dioxide A Year One of the most "
                        "stunning deforestation facts is that forest loss "
                        "contributes nearly 5 billion tons of carbon "
                        "dioxide into the atmosphere every year.",
                        "Brazil and Indonesia Account for Almost Half of "
                        "Tropical Deforestation That amounts to "
                        "approximately 1.7 million hectares each year. Both "
                        "Brazil and Indonesia are home to some of "
                        "the world’s largest and biodiversity tropical forests"
                        " in the world.",
                        "Animal feed makes "
                        "up 77% of soy production, while only 19.2% goes "
                        "directly into human food products. Globally, "
                        "soy is responsible for about 12% of deforestation. ",
                        "More Than 100 Countries Have Pledged to End "
                        "Deforestation by 2030 Despite the current state "
                        "of deforestation.",
                        "More than 100 countries "
                        "have joined a pledge to stop and reverse "
                        "deforestation by the end of the decade. Combined, "
                        "these 100+ countries make up 85% of the "
                        "world’s forests."]

list_of_option = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F',
                  'g', 'G', 'h', 'H', 'i', 'I']


# this function adds facts so when people are doing the quiz, they know some
# things about deforestation
def random_facts():
    random_deforestation = random.choice(list_of_random_facts)
    print("Did you know?", random_deforestation)


# this tells the user what is deforestation
def what_is():
    print("What is deforestation?")
    print("~~~~~~~~~~~~~~~~~~~~~~")
    print("Deforestation is the removal of a forest or stand of trees from "
          "land that is then converted to non-forest use like buildings, etc.")


# this function tells the user how to play the game
def how_to_play():
    print("This is a small quiz game where you need to answer the question "
          "about deforestation")
    print()
    print("The rules:")
    print("There are 10 question you need to answer")
    print("Answer the question by using the answers listed below")
    print("There will be some words that you won't know so there will be a "
          "list where it gives the definition")


# a loop where it keeps asking the user if they want to add a timer until they
# answer the question and if they don't, it will return to the function
def user_time():
    while True:
        # asking the user if they want to add a timer
        print("Press 1 for yes you want to use the timer")
        print("Or 2 for no timer")
        time_user = input("Do you wish to do a challenge where you have a"
                          " limited time to answer the question?")
        # if user said yes it will call the timer function
        if time_user == "1":
            timer()
            break
        # if the user said no, then it will call the main function
        elif time_user == "2":
            print("Continue")
            main()
            break
        else:
            print("Please choose 2 of the option")


# asked the user what they can do to reduce deforestation
def what_can_user_do():
    print("What can you do to reduce deforestation?")
    suggestion = ['Use less paper, plant trees or small plants, Buy recycled '
                  'products and then recycle them again'
                  'Buy certified wood products, Support the products of '
                  'companies that are committed to reducing deforestation.']
    print("=====================")
    print('You can', suggestion)
    print("____________________")
    print('Warning')
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print('If you are under 18, make sure you asked your guardian or parent '
          'permission first before doing those')


# asking the user question which is a loop, and it will keep asking again
# until they choose one of the option which is y, yes or n, no
def play_again():
    while True:
        play = input("Do you wish to play the quiz again?")
        if play == "yes" or play == "y":
            user_time()
            print("Welcome back to the quiz")
            break
        elif play == "Yes" or play == "Y":
            user_time()
            print("Welcome back to the quiz")
            break
        elif play == "no" or play == "n":
            print("------------------------------")
            print("Thank you for playing the quiz")
            print("------------------------------")
            exit(0)
        elif play == "No" or play == "N":
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
             'question9': 'What will happen to the animals in the forest if it'
                          ' is destroyed?',
             'question10': 'What will be the future for the Earth if the '
                           'forest is gone?'}
answer = {'answers': 'a', 'answer2': 'c', 'answer3': 'b', 'answer4': 'e',
          'answer5': 'd', 'answer6': 'f', 'answer7': 'h', 'answer8': 'g',
          'answer9': 'i', 'answer10': 'j'}

# list of answers where the user will see the list of answers which they will
# answer them
list_of_answer1 = ["A = Human activity", "B = logging, agriculture, "
                                         "overpopulation, etc.",
                   "C = The forest is a water cycle, soil, home to many animals"
                   " and the source of oxygen and clean water",
                   "D = Plant a tree, use less paper, reuse paper or cardboard",
                   "E = The loss of trees and other vegetation can cause "
                   "flooding, increased greenhouse gases",
                   "F = They purify the air we breathe, filter the water we "
                   "drink, prevent erosion, and act as an important buffer "
                   "against climate change."]

list_of_answer2 = ["G =The absence of trees would result in significantly "
                   "HIGHER amounts of carbon dioxide in the air and LOWER "
                   "amounts of oxygen!",
                   "H = 100 years"
                   "I =  It causes habitat destruction, reduced food "
                   "availability, and much more.",
                   "J = There would be massive extinctions of all groups of "
                   "organisms, both locally and globally."]

random.shuffle(list_of_answer1)
random.shuffle(list_of_answer2)

meaning = ["Erosion is the action of surface processes that removes soil and"
           "moves it to another place ",
           "Greenhouse gases (also known as GHGs) are gases in the Earth's "
           "atmosphere that trap heat"]


# one of the def where it asked the user the questions
def question_1():
    print("``````````````")
    random_facts()
    print("@@@@@@@@@@@@@")
    # these print the list that are on the top which
    # will be the list of answers, the facts and meaning
    print(list_of_answer1)
    print("%%%%%%%%%%%%%%%")
    print(list_of_answer2)
    print("???????????????")
    print(meaning)
    # this inputs the question in the dictionary with the first question
    user_question = input(questions['questions'])
    user_question = user_question.lower()
    # if the users answer are not on the list which is the option, then
    # it will print the options and will return to the function until
    # they choose the options in the list
    if user_question not in list_of_option:
        print("-------------------------------")
        print("Please choose one of the option")
        return question_1()
    elif user_question == answer['answers'] or user_question == "A":
        # a global variable in Python means having a scope throughout
        # the program which in this case, the scores are the global
        global num_of_scores
        num_of_scores += 1
        print("********")
        print("Correct!")
    else:
        print("#########")
        print("Incorrect")
        # else will give the user to pass and go on to the next questions
        pass


def question_2():
    print("`````````````")
    random_facts()
    print("@@@@@@@@@@@@@")
    print(list_of_answer1)
    print("%%%%%%%%%%%%%%%")
    print(list_of_answer2)
    print("???????????????")
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
    random_facts()
    print("@@@@@@@@@@@@@")
    print(list_of_answer1)
    print("%%%%%%%%%%%%%%%")
    print(list_of_answer2)
    print("???????????????")
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
    random_facts()
    print("@@@@@@@@@@@@@")
    print(list_of_answer1)
    print("%%%%%%%%%%%%%%%")
    print(list_of_answer2)
    print("???????????????")
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
    random_facts()
    print("@@@@@@@@@@@@@")
    print(list_of_answer1)
    print("%%%%%%%%%%%%%%%")
    print(list_of_answer2)
    print("???????????????")
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
    random_facts()
    print("@@@@@@@@@@@@@")
    print(list_of_answer1)
    print("%%%%%%%%%%%%%%%")
    print(list_of_answer2)
    print("???????????????")
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
    random_facts()
    print("@@@@@@@@@@@@@")
    print(list_of_answer1)
    print("%%%%%%%%%%%%%%%")
    print(list_of_answer2)
    print("???????????????")
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
    random_facts()
    print("@@@@@@@@@@@@@")
    print(list_of_answer1)
    print("%%%%%%%%%%%%%%%")
    print(list_of_answer2)
    print("???????????????")
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
    random_facts()
    print("@@@@@@@@@@@@@")
    print(list_of_answer1)
    print("%%%%%%%%%%%%%%%")
    print(list_of_answer2)
    print("???????????????")
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
    random_facts()
    print("@@@@@@@@@@@@@")
    print(list_of_answer1)
    print("%%%%%%%%%%%%%%%")
    print(list_of_answer2)
    print("???????????????")
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


# if the user pressed no on the user_time,
# it calls this function
def main():
    for i in range(1, 10):
        str1 = f"question_{i}()"
        print(str1)

        eval(str1)  # call function

    print("You got {}/10".format(num_of_scores))
    what_can_user_do()
    play_again()


my_timer = 10


# when the user_time is yes, then
# it calls this function
def timer():
    def countdown():
        global my_timer
        # this is the time that the user have which
        # is 10 seconds
        my_timer = 10

        for x in range(10):
            my_timer = my_timer - 1
            sleep(1)
        print("!!!!!!!!!!!!!!!!!!!!!!!!")
        print("You have run out of time")
        print("You got {}/10".format(num_of_scores))
        what_can_user_do()
        print("<><><><><><><><><><><>")
        print("Please enter yes or no")
        print("Again when question appear")
        play_again()

    countdown_thread = threading.Thread(target=countdown)

    countdown_thread.start()

    # this a loop where the timer is bigger than 0
    # starts the timer where it then - 1 each time
    # until it hits 0
    while my_timer > 0:

        print("//////////////////////////////////////////")
        print("You have 10 seconds to answer the question")
        print("//////////////////////////////////////////")

        for i in range(1, 10):
            str2 = f"question_{i}()"
            print(str2)

            eval(str2)  # call function

        # if my_timer hits 0, it will break the loop
        if my_timer == 0:
            break


# the main part of the game
name_user = input("Hello user, this is a little quiz about deforestation "
                  "what is your name?")
print("☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻")
print("Hello {}".format(name_user).title())
what_is()
print("{}{}{}{}{}{}{}{}{}{}{}{}{}")
how_to_play()
print("{}{}{}{}{}{}{}{}{}{}{}{}{}")
user_time()
print("{}{}{}{}{}{}{}{}{}{}{}{}{}")
play_again()
