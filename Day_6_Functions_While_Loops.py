# Reeborg's World
# Hurdle 1
# https://reeborg.cs20.ca/?lang=en&mode=python&menu=%2Fworlds%2Fmenus%2Fsk_menu.json&name=Hurdle%201&url=%2Fworlds%2Ftutorial_en%2Fhurdle1.json

"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_one_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for steps in range(0,6):
    jump_one_hurdle()
"""

# Pythons recommends using 4 spaces for indentation
# Tab can also be used
# In Python 3, you can mix spaces and tabs for indentation

# Reeborg's World
# Hurdle 2
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_one_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()    
    
while not at_goal():
    jump_one_hurdle()
"""


# Reeborg's World
# Hurdle 3
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_one_hurdle():
    #move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()    
    
while not at_goal():
    if wall_in_front():
        jump_one_hurdle()
    else:
        move()
"""

# Reeborg's World
# Hurdle 4
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_one_hurdle():
    #move()
    turn_left()
    move()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()    
    
while not at_goal():
    if wall_in_front():
        jump_one_hurdle()
    else:
        move()
"""