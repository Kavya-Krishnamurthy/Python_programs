

from karel.stanfordkarel import *

def main():
    """
    Put 10 beepers in every cell in the bottom row of the world.
    """
    while front_is_clear():
        indent_beeper()
        move()
    indent_beeper()

def indent_beeper():
    for i in range(10):
            put_beeper()   


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
