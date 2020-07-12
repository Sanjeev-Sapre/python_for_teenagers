import turtle
import random

turtle.setup (width=800, height=400)
turtle.colormode(255)
turtle.bgcolor(167, 143, 124)


# set up the players
player1 = turtle.Turtle()
player1.shape("turtle")
player1.color("green")
player2 = player1.clone()
player2.color("blue")

# set up the end line for the race.
gk = turtle.Turtle()
gk.penup()
gk.hideturtle()
gk.goto(300, 160)
gk.right(90)
gk.pendown()
gk.pencolor('black')
gk.pensize(2)
gk.forward(320)
gk.penup()
gk.goto( -390, 170)
gk.write("Turtle Race Game -" ,True, font=("Arial", 14, "bold") )
gk.write(" Now Playing :" ,True, font=("Arial", 14, "normal") )



# take them to starting points
player1.hideturtle()
player1.penup()
player1.goto(-300, 100)
player1.showturtle()

player2.hideturtle()
player2.penup()
player2.goto(-300, -100)
player2.showturtle()

die = [1, 2, 3, 4, 5, 6]

for i in range(20):
    if player1.pos() >= (300, 100):
        print("Player One Wins!")
        break
    elif player2.pos() >= (300, -100):
        print("Player Two Wins!")
        break


for i in range(20):
    if player1.pos() >= (300, 100):
        print("Player One Wins!")
        break
    elif player2.pos() >= (300, -100):
        print("Player Two Wins!")
        break
    else:
        player1_turn = input("Press 'Enter' to roll the die ")
        #gk.write(" Player1 " ,font=("Arial", 14, "normal") )
        die_outcome = random.choice(die)
        print("The result of the die roll for player 1 is: ", die_outcome)
        print("The number of steps will be: " , 20*die_outcome)
        player1.fd(20*die_outcome)

        player2_turn = input("Press 'Enter' to roll the die ")
        #gk.write(" Player 2 " ,font=("Arial", 14, "normal") )
        die_outcome = random.choice(die)
        print("The result of the die roll fpr player 2 is: " , die_outcome)
        print("The number of steps will be: " , 20*die_outcome)
        player2.fd(20*die_outcome)