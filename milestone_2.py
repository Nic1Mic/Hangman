import random

#Created a list of  5  fruits
favorite_fruits = ["Apple", "Banana", "Cherry", "Strawberry", "Pineapple"]

#Assigned the list to a variable called word_list
word_list = favorite_fruits

#Print out the newly created list
print("Word List:", word_list)

#Used random.choice to select a random word
word = random.choice(word_list)

#Print out the randomly generated word
print("Randomly Generated Word:", word)

#User input
user_input = input("Guess a letter: ")

#Checking if the input is a single alphabetical character
if len(user_input) == 1 and user_input.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
    