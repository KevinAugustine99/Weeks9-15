"""
tree_drawing_week03.py
Author: Kevin Augustine

Tree-drawing example from class, slightly modified
"""

import turtle

# How many little branches each branch has
BRANCHES = 3

INIT_OFFSET = 200 # how far down to move initially
TRUNK_LENGTH = 200 #length of tree's main trunk
DEPTH = 5 # how "deep" to go
SPEED = 0 # how quickly to draw

# How far apart the branches will be
FULL_TURN = (360 / ( BRANCHES + 1 ) )

# How much to turn at the beginning to start drawing the first branch
# (works for how much to turn back when done, too
STARTING_TURN = FULL_TURN * ( BRANCHES - 1 ) / 2 

def draw_tree( t: turtle.Turtle, levels: int, length: float ):
    if levels == 0:
        pass
    elif levels == 1:
        t.forward( length )
        t.backward( length )
    else:
        t.forward( length )
        t.left( STARTING_TURN )
        draw_tree( t, levels - 1, length / 2 )
        t.right( FULL_TURN )
        draw_tree( t, levels - 1, length / 2 )
        t.right( FULL_TURN )
        draw_tree( t, levels - 1, length / 2 )
        t.left( STARTING_TURN )
        t.backward( length )

def main():
    # Create a new turtle object. (Helps in PyCharm.)
    t = turtle.Turtle()

    t.speed( SPEED )

    # Set up the turtle.
    t.left( 90 )
    t.penup()
    t.back( INIT_OFFSET )
    t.pendown()

    # Do the drawing.
    draw_tree( t, DEPTH, TRUNK_LENGTH )

    turtle.done()

if __name__ == "__main__":
    # main() will not execute if this file is imported rather than run directly.
    main()
