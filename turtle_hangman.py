import turtle
from turtle import done
import random

word_list = ["ENTER", "SHOUT", "WORD", "LOCOMOTIVE", "TECHNOLOGY", "TURTLE", "PROGRAMMING", "SECURITY", "DESIGN", "ANIMATION", "HACKING", "ROCKET", "ENGINEER", "SCIENCE", "POKEMON", "FORTNITE", "BRAINROT", "SKIBIDI", "TOILET"]
secret_answer = random.choice(word_list) #Selects a random word from the list above
guessed_input = ["_"] * len(secret_answer) #this will print the amount of _ according to the length of the answer

wrong_tries = 0
max_tries = 6

# opening a screen for Turtle, using in build turtle method.

screen = turtle.Screen()
screen.title("Eric's Hangman")
screen.setup(width=1920, height=1080)
screen.bgcolor("Black")

# Settings for the "pen"

pen = turtle.Turtle()
pen.pensize(5)
pen.color("White")
pen.speed(5)


# Function for the Gallows

def draw_gallows():
    pen.penup() # Can purposefully leave this one out for kids to figure out whats wrong if this is left out
    pen.goto(0, 300)
    pen.pendown() # Same with this one, can leave out for kids to figure out
    pen.left(90)
    pen.forward(200)
    pen.left(90)
    pen.forward(400)
    pen.left(90)
    pen.forward(900)
    pen.left(90)
    pen.forward(800)

draw_gallows()


# Function for the man
def draw_hangman(tries): # has arg "tries" because you want to draw the hangman as you get stuff wrong., dont want to draw it straight away
    if tries == 1: #drawing head
        pen.penup()
        pen.goto(0, 200)
        pen.pendown()
        pen.circle(50) #radius
    elif tries == 2: #body
        pen.penup()
        pen.goto(0, 200)
        pen.pendown()
        pen.right(90)
        pen.forward(300)
    elif tries == 3: # Left hand
        pen.penup()
        pen.goto(0, 150)
        pen.pendown()
        pen.right(45)
        pen.forward(150)
    elif tries == 4: # Right Hand
        pen.penup()
        pen.goto(0, 150)
        pen.pendown()
        pen.left(90)
        pen.forward(150)
    elif tries == 5: #Left Leg
        pen.penup()
        pen.goto(0, -100)
        pen.pendown()
        pen.right(90)
        pen.forward(150)
    elif tries == 6: #Right Leg
        pen.penup()
        pen.goto(0, -100)
        pen.pendown()
        pen.left(90)
        pen.forward(150)
    


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

guessed_letters = []
guessed_pen = turtle.Turtle()
word_pen = turtle.Turtle() #need to define this because if not then .clear() will clear the hangman

while wrong_tries < max_tries:
    guess = screen.textinput("Type a Letter: ", "").upper() #input validation
    if not guess or not guess.isalpha() or len(guess) != 1: #always check for empty input before string methods
        print("Please enter a single alphabet")
        continue
    
    guessed_letters.append(guess)

    if guess in secret_answer:
        for i, letter in enumerate(secret_answer): #if there are multiple of the same letter in my word, it will update and pop up
            if letter == guess:
                guessed_input[i] = guess
                print(f"Nice one! ", (guessed_input))
                word_pen.clear()
                word_pen.color("White")
                word_pen.penup()
                word_pen.goto(0, -800)
                word_pen.write(f"{guessed_input}", align = "Center", font = ("Courier" , 25, "bold"))

    else:
        wrong_tries += 1
        draw_hangman(wrong_tries)
        guessed_pen.penup()
        guessed_pen.color("White")
        guessed_pen.goto(0, -600)
        guessed_pen.clear()
        guessed_pen.write(f"Guessed: {guessed_letters}", align = "center", font=("Courier", 18, "bold"))
        print("Wrong! Try again")

    
    if wrong_tries == max_tries:
        lose_screen()
        break
    if "_" not in guessed_input:
        win_screen()
        break  # what happens if i leave this out?
    


done()




    

