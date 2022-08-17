print("What can you do to reduce deforestation?")
suggestion = ['Use less paper, plant trees or small plants, Buy recycled '
              'products and then recycle them again'
              'Buy certified wood products, Support the products of companies '
              'that are committed to reducing deforestation.']
print('You can', suggestion)
print('Warning')
print('If you are under 18, make sure you asked your guardian or parent '
      'permission first before doing those')


# asking the user question
def play_again():
    play = input("Do you wish to play the quiz again?")
    if play == "yes" or play == "y":
        print("Welcome back to the quiz ")
    elif play == "no" or play == "n":
        print("------------------------------")
        print("Thank you for playing the quiz ")
        print("------------------------------")
        exit(0)
    else:
        print("Please choose one of the option?")
        return play_again()


play_again()
