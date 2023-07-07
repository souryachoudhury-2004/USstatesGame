import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
screen.setup(height=491, width=725)

cursor = turtle.Turtle()
image = "blank_states_img.gif"
screen.addshape(image)
cursor.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []


while len(guessed_states) < 50:
    answer_state = turtle.textinput(title=f"{len(guessed_states)}/50 States Guessed.", prompt="What's another US state?")
    answer_state = answer_state.title()

    # Exit condition
    if answer_state in ["Exit", "Quit", "Close"]:
        break

    # If answer state is one of the states in 50 states
    if answer_state in all_states:
        guessed_states.append(answer_state)
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        state_data = data[data.state == answer_state]
        writer.goto(int(state_data.x), int(state_data.y))
        writer.write(state_data.state.item(), align="center", font=("Times New Roman", 12, "normal"))

# Generating states to learn
missed_states = []

for state in all_states:
    if state not in guessed_states:
        missed_states.append(state)

# Writing to text file
with open("Missed_States.txt", "w") as file:
    file.writelines("Missed States: \n")
    for item in missed_states:
        file.write(item+"\n")

screen.exitonclick()