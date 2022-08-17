score = 0
# the dictionary for the quiz
question = {'questions': 'What is the cause of deforestation?', 'question2':'Why is the forest important?',
            'question3': 'Why do deforestation happen?', 'question4': 'What are the aftermath of the effects',
            'question5': 'How to reduce deforestation?',
            'question6': 'Why should be care about deforestation?'}
answer = {'answers': 'a', 'answer2': 'b', 'answer3': 'c', 'answer4': 'e', 'answer5': 'd', 'answer6': 'f'}

# list of answers where the user will see the list of answers
list_of_answer = ["A = Human activity", "B = The forest is a water cycle, soil, home to many animals and the source of"
                                        "oxygen, water and clean water which is what living beings need to survive."
                                        "erosion, and act as an important buffer against climate change.",
                  "C = The reasons for deforestation are logging, agriculture, cattle ranching, overpopulation, etc.",
                  "D = Plant a tree, use less paper, reuse paper or cardboard", "F = They purify the air we breathe, "
                                                                                "filter the water we drink, prevent "
                                                                                "erosion, and act as an important "
                                                                                "buffer against climate change."]

# main
print(list_of_answer)
user_question = input(question['questions'])
if user_question == answer['answers']:
    score += 1
    print("Correct! ")
elif user_question == answer:
    print("Wrong answer")
else:
    print("Please choose one of the option")

user_question = input(question['question2'])
if user_question == answer['answer2']:
    print("Correct! ")
    score += 1
elif user_question == answer:
    print("Wrong answer")
else:
    print("Please choose one of the option")

user_question = input(question['question3'])
if user_question == answer['answer3']:
    score += 1
    print("Correct! ")
elif user_question == answer:
    print("Wrong answer")
else:
    print("Please choose one of the option")

user_question = input(question['question4'])
if user_question == answer['answer4']:
    score += 1
    print("Correct! ")
elif user_question == answer:
    print("Wrong answer")
else:
    print("Wrong answer")

user_question = input(question['question5'])
if user_question == answer['answer5']:
    score += 1
    print("Correct! ".format(score))
elif user_question == answer:
    print("Wrong answer")
else:
    print("Please choose one of the option")

user_question = input(question['question6'])
if user_question == answer['answer6']:
    score += 1
    print("Correct! ".format(score))
elif user_question == answer:
    print("Wrong answer")
else:
    print("Please choose one of the option")

print("You have {}/6".format(score))
