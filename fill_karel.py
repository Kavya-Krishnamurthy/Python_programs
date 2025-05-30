"""task is to help Karel fill the world with beepers, regardless of its size.EX: 5x5, 3x4 ,2X2"""


from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        place_beepers()
        turn_back()
        move_next()
    

def place_beepers():
    put_beeper()
    while facing_east():
        if front_is_clear():
            move()
            put_beeper()
        else:
            turn_around()

def turn_back():
    while facing_west():
        if front_is_clear():
            move()
        else:
            turn_right()

def move_next():
    if front_is_clear():
        move()
        turn_right()
    else:
        turn_right()
        while front_is_clear():
            move()
                

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
