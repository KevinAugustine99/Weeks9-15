"""
File : ball_puzzle.py
Assignment : Lab #9
Language : python3
Author : Kevin Augustine < kea4437@rit.edu >
"""

from ball_puzzle_animate import *
from stack import *
from node import *
from time import sleep

def make_stack_list(input_string):
    """make_stack_list makes and returns the list of stacks which has all of the balls in the red stack and the green and the blue stacks are empty
        input_string: the input string where each character is a ball in the red can
        stack_list: the list of stacks(cans), index 0 (the red can), index 1 (the green can), index 2 (the blue can)
        x: each character/ball in the input string
    """
    stack_list = [make_empty_stack(),make_empty_stack(),make_empty_stack()]
    for x in input_string:
        #Each character/ball in the input string is pushed into the red can/stack
        push(stack_list[0],x)
    return stack_list

def move_ball(stack_list, from_can, to_can):
    """move_ball takes the top ball from from_can and puts it into to_can and then animates it
        stack_list: the list of stacks(cans), index 0 (the red can), index 1 (the green can), index 2 (the blue can)
        from_can: the index for the stack(can) that the ball is being taken out of
        to_can: the index for the stack(can) that the ball is going into
        ball: the ball being transfered from one can to another
    """
    ball = pop(stack_list[from_can])
    push(stack_list[to_can], ball)
    animate_move(stack_list,from_can,to_can)

def empty_red(stack_list):
    """empty_red empties the red can and puts the blue and red balls into the blue can and puts the green balls into the green can
        stack_list: the list of stacks(cans), index 0 (the red can), index 1 (the green can), index 2 (the blue can)
    """
    while size(stack_list[0]) != 0:
        #While the red can is not empty
        if top(stack_list[0]) == "G":
            #If the ball is green, then the ball goes into the the green can
            move_ball(stack_list,0,1)
        else:
            #If the ball is not green, then the ball goes into the blue can
            move_ball(stack_list,0,2)

def empty_blue(stack_list):
    """empty_blue empties the blue can and puts the red balls into the red can and puts the blue balls into the green can
        stack_list: the list of stacks(cans), index 0 (the red can), index 1 (the green can), index 2 (the blue can)
    """
    while size(stack_list[2]) != 0:
        #While the blue can is not empty
        if top(stack_list[2]) == "R":
            #If the ball is red then the ball goes into the red can
            move_ball(stack_list,2,0)
        else:
            #If the ball is not red then the ball goes into the green can
            move_ball(stack_list,2,1)

def sort_green(stack_list):
    """sort_green takes all of the blue balls out of the green can and puts it into the blue can
        stack_list: the list of stacks(cans), index 0 (the red can), index 1 (the green can), index 2 (the blue can)
    """
    while top(stack_list[1]) == "B":
        #While the ball is blue, move the ball to the green can
        move_ball(stack_list,1,2)

def solve(input_string):
    """solve creates the stack_list, solves the puzzle, and returns the amount of moves it takes to complete the puzzle
        input_string: the input string where each character is a ball in the red can
        stack_list: the list of stacks(cans), index 0 (the red can), index 1 (the green can), index 2 (the blue can)
    """
    stack_list = make_stack_list(input_string)
    empty_red(stack_list)
    empty_blue(stack_list)
    sort_green(stack_list)
    return (2 * size(stack_list[0])) + (size(stack_list[1])) + (3*(size(stack_list[2])))

def main():
    input_string = input("What balls are in the red can?")
    animate_init(input_string)
    # sleep(10)
    number_of_moves = solve(input_string)
    print("The number of moves to solve this puzzle is",number_of_moves)
    print("Close the window to quit")
    animate_finish()

if __name__ == "__main__":
    main()