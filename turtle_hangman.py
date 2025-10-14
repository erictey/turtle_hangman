import turtle
from turtle import done
import random

word_list = ["ENTER", "SHOUT", "LOCOMOTIVE", "TECHNOLOGY", "TURTLE", "PROGRAMMING", "SECURITY", "DESIGN",
             "ANIMATION", "HACKING", "ROCKET", "ENGINEER", "SCIENCE", "POKEMON", "FORTNITE", "BRAINROT", "SKIBIDI", "TOILET"]
# Selects a random word from the list above
secret_answer = random.choice(word_list)
# this will print the amount of _ according to the length of the answer
guessed_input = ["_"] * len(secret_answer)

wrong_tries = 0
max_tries = 6

# settings for the screen for Turtle, using in build turtle method.

screen = turtle.Screen()
screen.title("Eric's Hangman")
screen.setup(width=1920, height=1080)
screen.bgcolor("Black")

# Settings for the "pen"

pen = turtle.Turtle()
pen.pensize(5)
pen.color("White")
pen.speed(0)  # 0 is instant


# Function for the Gallows


def draw_gallows():
    pen.penup()
    pen.goto(0, 300)
    pen.pendown()
    # zip is a built in function that allows u to loop through 2 lists at the same time
    for angle, distance in zip([90, 90, 90, 90], [200, 400, 900, 800]):
        pen.left(angle)
        pen.forward(distance)


draw_gallows()


# Function for the man
# has arg "wrong_tries because you want to draw the hangman as you get stuff wrong., dont want to draw it straight away
def draw_hangman(wrong_tries):
    if wrong_tries == 1:  # drawing head
        pen.penup()
        pen.goto(0, 200)
        pen.pendown()
        pen.circle(50)  # radius
    elif wrong_tries == 2:  # body
        pen.penup()
        pen.goto(0, 200)
        pen.pendown()
        pen.right(90)
        pen.forward(300)
    elif wrong_tries == 3:  # Left hand
        pen.penup()
        pen.goto(0, 150)
        pen.pendown()
        pen.right(45)
        pen.forward(150)
    elif wrong_tries == 4:  # Right Hand
        pen.penup()
        pen.goto(0, 150)
        pen.pendown()
        pen.left(90)
        pen.forward(150)
    elif wrong_tries == 5:  # Left Leg
        pen.penup()
        pen.goto(0, -100)
        pen.pendown()
        pen.right(90)
        pen.forward(150)
    elif wrong_tries == 6:  # Right Leg
        pen.penup()
        pen.goto(0, -100)
        pen.pendown()
        pen.left(90)
        pen.forward(150)


# I want it to pop up in your face that you have failed to guess the correct word. You must never forget your incompetence.
def win_screen():
    pen.hideturtle()
    pen.color("Green")
    pen.penup()
    pen.goto(0, 0)
    pen.write(f"ERIC LIVES, YOUR WORD WAS: {secret_answer}",
              align="center",
              font=("Courier", 30, "bold")
              )


def lose_screen():
    pen.hideturtle()
    pen.color("Red")
    pen.penup()
    pen.goto(0, 0)
    pen.write(f"ERIC HAS DIED, YOUR WORD WAS: {secret_answer}",
              align="center",
              font=("Courier", 30, "bold")
              )


guessed_letters = []  # Stores guessed letters in a string, updates on line 126
guessed_pen = turtle.Turtle()
# need to define these because if not then .clear() will clear the hangman
word_pen = turtle.Turtle()

while wrong_tries < max_tries:  # While the player is still in game
    # makes a window for text input
    guess = screen.textinput("Type a Letter: ", "").upper()
    # INPUT VALIDATION!! always check for empty input before string methods i
    if not guess or not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet")
        continue

    # Adds the guessed letters to guessed_letters
    guessed_letters.append(guess)

    # it is important to index (i). if say secret_answer was "hello", list(enumerate(secret_answer) --> (0, H), (1, E), (2, L) etc etc
    if guess in secret_answer:  # If the letter is found in secret_answer
        # this means go through every character in secret_answer, starting from i (0, ie the first letter), and return the letter and the position.
        for i, letter in enumerate(secret_answer):
            if letter == guess:  # checks if the guessed letter is in every single position of the secret word
                # changes guessed_input to the letter at the correct i position
                guessed_input[i] = guess
                print(f"Nice one! ", (guessed_input))
                word_pen.clear()
                word_pen.color("White")
                word_pen.penup()
                word_pen.goto(0, -600)
                word_pen.write(f"{guessed_input}",
                               align="Center", font=("Courier", 25, "bold"))

    else:
        wrong_tries += 1  # adds 1 to wrong_tries
        draw_hangman(wrong_tries)  # starts from step 1
        guessed_pen.penup()
        guessed_pen.color("White")
        guessed_pen.goto(0, -500)
        guessed_pen.clear()
        guessed_pen.write(
            f"Guessed: {guessed_letters}", align="center", font=("Courier", 18, "bold"))
        print("Wrong! Try again")

    if wrong_tries == max_tries:
        lose_screen()
        break
    if "_" not in guessed_input:  # When all "_" are filled out ie u won
        win_screen()
        break  # what happens if i leave this out?


done()
