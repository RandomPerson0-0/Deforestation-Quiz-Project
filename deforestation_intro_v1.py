
def facts_about_deforestation():
    print("What is deforestation?")
    print()
    print("Deforestation is the removal of a forest or stand of trees from "
          "land that is then converted to non-forest use like buildings, etc.")


# how to play the game
def how_to_play():
    print("This is a small quiz game where you need to answer the question "
          "about deforestation")
    print()
    print("The rules:")
    print("There are 10 question you need to answer")
    print("Answer the question by using the answers listed below")
    print("There will be some words that you wont know so there will be a "
          "list where it gives the definition")


name_user = input("Hello user, this is a little quiz about deforestation "
                  "what is your name?")
print("Hello {}".format(name_user).title())

facts_about_deforestation()

print("The quiz continues")

how_to_play()
