import turtle
import pandas

tim= turtle.Turtle()
tim.hideturtle()
tim.penup()

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_guessed = []
state_data = pandas.read_csv("50_states.csv")
states_names = state_data.state.to_list()


while len(states_guessed) != 50:
    answer_state = screen.textinput(title=f"States guessed {len(states_guessed)}/50",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in states_names if state not in states_guessed]

        data = pandas.DataFrame(missing_states)
        data.to_csv("States_to_learn.csv")
        break

    if answer_state in states_names:
        states_guessed.append(answer_state)

        guess_data = state_data[state_data.state == answer_state]
        x_cord = guess_data.x.item()
        y_cord = guess_data.y.item()

        tim.goto(x_cord, y_cord)
        tim.write(arg= answer_state, align= "center", font=("Arial", 10, "normal" ))


screen.exitonclick()