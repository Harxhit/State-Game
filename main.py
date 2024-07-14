import turtle 
import pandas  

screen = turtle.Screen()
screen.title("State Game!")


image = "C:\\Users\\Welcome\\OneDrive\\Desktop\\Python\\Mini Project\\State-game\\blank_states_img.gif"


screen.addshape(image)


turtle.shape(image)

"""How to get coordinates of states"""
# def get_mouse_click_cor(x, y ) :
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_cor)



data = pandas.read_csv("C:\\Users\\Welcome\\OneDrive\\Desktop\\Python\\Mini Project\\State-game\\50_states.csv")

all_states = data.state.str.lower().to_list()


guess_state = []

while len(guess_state) < 50 :

  answer = screen.textinput(title=f"{len(guess_state)}/50" , prompt= "What is the name of other state?").lower()
  
  if answer :
    answer_lower = answer.lower()
  if answer == "exit" :
    missing_states = [state for state in all_states if state not in guess_state]
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("states_to_lear.csv")
    break
  
  if answer_lower in all_states :
    guess_state.append(answer_lower)
    timmy = turtle.Turtle()
    timmy.hideturtle()
    timmy.penup()
    state_data = data[data.state.str.lower() == answer_lower]
    timmy.goto(state_data.x.item() , state_data.y.item())
    timmy.write(answer.lower())




#states_to_learn.csv 




