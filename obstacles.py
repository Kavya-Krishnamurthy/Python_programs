

from karel.stanfordkarel import *

def main():
    """
    Karel starts facing East in the bottom left corner of the world and ends facing East in the bottom right corner of the world.
    """
    move()
    for i in range(3):
        fill_square()
    move()
    move()

def fill_square():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    put_beeper()
    turn_left()
    


def turn_right():
    turn_left()
    turn_left()
    turn_left() 


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
