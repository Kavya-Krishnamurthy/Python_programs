from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        build_cols()
        if front_is_clear():
            move_to_next_spot()
    build_cols()
        
        
def build_cols():
    turn_left()
    for i in range(5):
        put_beeper()
        if front_is_clear():
            move()
    turn_back()
    for j in range(5):
        if front_is_clear():
            move()
    turn_left()


def move_to_next_spot():
    for i in range(4):
        if front_is_clear():
            move()
    
        
def turn_right():
    for i in range(3):
        turn_left()


def turn_back():
    turn_left()
    turn_left()
        
if __name__ == '__main__':
    main()