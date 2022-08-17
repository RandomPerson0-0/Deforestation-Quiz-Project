# asking the user there name
name_user = input("Hello user, this is a little quiz about deforestation "
                  "what is your name?")
# .title uses capital on the first letter and the format put the title of the input into the {}
print("Hello {}".format(name_user).title())


# asking the user question
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "Yes"
            return response

        elif response == "no" or response == "n":
            response = "No"
            return response
        else:
            print("Please answer yes/no")


# this tells the user what is deforestation
def facts_about_deforestation():
    print("What is deforestation?")
    print()
    print("Deforestation is the removal of a forest or stand of trees from "
          "land that is then converted to non-forest use like buildings, etc.")


# this is one of the function that shows how to play the game
def how_to_play():
    print("This is a small quiz game where you need to answer the question "
          "about deforestation")
    print()
    print("The rules:")
    print("There are 10 question you need to answer")
    print("Answer the question by using the answers listed below")
    print("There will be some words that you wont know so there will be a "
          "list where it gives the definition")


# asking the user if they know about deforestation
user = yes_no("Do you know about deforestation {}?".format
              (name_user).title())
if user == 'no' or user == 'n':
    facts_about_deforestation()

print("The quiz continues")
# these calls the function at the top
how_to_play()
