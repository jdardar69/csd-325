"""Forest Fire Simulation with Lake Firebreak
Module 6.2 Assignment - CSD-325 Advanced Python
Modified by Jordan Dardar

Original program by Al Sweigart, with prior modifications by Sue Sampson.
This version adds a lake feature in the center of the display that acts
as a firebreak. The water cells:
  * Use a different character from trees and fire.
  * Are displayed in blue.
  * Never change once created (no trees grow there, and they never burn).
"""

import random
import sys
import time

try:
    import bext
except ImportError:
    print("This program requires the bext module, which you")
    print("can install by following the instructions at:")
    print("https://pypi.org/project/Bext/")
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = "A"
FIRE = "@"
EMPTY = " "
WATER = "~"   # New constant for the lake / water feature.

# Try changing these settings to anything between 0.0 and 1.0:
INITIAL_TREE_DENSITY = 0.20  # Amount of forest that starts with trees.
GROW_CHANCE = 0.01           # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.01           # Chance a tree is hit by lightning & burns.

# Try setting the pause length to 1.0 or 0.0:
PAUSE_LENGTH = 0.5


def main() -> None:
    """Run the forest fire simulation."""
    forest = create_new_forest()
    bext.clear()

    # Main program loop.
    while True:
        display_forest(forest)

        # Run a single simulation step:
        next_forest = {"width": forest["width"], "height": forest["height"]}

        for x in range(forest["width"]):
            for y in range(forest["height"]):
                if (x, y) in next_forest:
                    # If we've already set next_forest[(x, y)] on a
                    # previous iteration, just skip it here.
                    continue

                cell = forest[(x, y)]

                # NEW BEHAVIOR: Water never changes.
                if cell == WATER:
                    next_forest[(x, y)] = WATER
                    continue

                # Grow a tree in this empty space.
                if (cell == EMPTY) and (random.random() <= GROW_CHANCE):
                    next_forest[(x, y)] = TREE

                # Lightning sets this tree on fire.
                elif (cell == TREE) and (random.random() <= FIRE_CHANCE):
                    next_forest[(x, y)] = FIRE

                # This tree is currently burning.
                elif cell == FIRE:
                    # Loop through all the neighboring spaces:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            neighbor = (x + ix, y + iy)
                            # Fire spreads to neighboring trees only.
                            if forest.get(neighbor) == TREE:
                                next_forest[neighbor] = FIRE
                    # The tree has burned down now, so erase it:
                    next_forest[(x, y)] = EMPTY

                # Otherwise, just copy the existing object.
                else:
                    next_forest[(x, y)] = cell

        forest = next_forest
        time.sleep(PAUSE_LENGTH)


def create_new_forest():
    """Return a dictionary for a new forest data structure.

    The forest dictionary stores width and height, plus a mapping
    from (x, y) coordinate tuples to cell contents.
    This function also adds a lake of WATER cells in the middle of
    the grid that acts as a permanent firebreak.
    """
    forest = {"width": WIDTH, "height": HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Randomly decide whether this position starts as a tree.
            if (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE  # Start as a tree.
            else:
                forest[(x, y)] = EMPTY  # Start as an empty space.

    # Add a rectangular lake roughly in the center of the display.
    add_central_lake(forest)
    return forest


def add_central_lake(forest) -> None:
    """Modify the forest in-place to add a central lake of WATER cells.

    The lake is a rectangle placed roughly in the center of the grid.
    These cells become WATER and will never change during the simulation.
    """
    lake_width = 9
    lake_height = 5

    # Compute the top-left corner so the lake is centered.
    start_x = max(0, forest["width"] // 2 - lake_width // 2)
    start_y = max(0, forest["height"] // 2 - lake_height // 2)

    end_x = min(forest["width"], start_x + lake_width)
    end_y = min(forest["height"], start_y + lake_height)

    for x in range(start_x, end_x):
        for y in range(start_y, end_y):
            forest[(x, y)] = WATER


def display_forest(forest) -> None:
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for y in range(forest["height"]):
        for x in range(forest["width"]):
            cell = forest[(x, y)]
            if cell == TREE:
                bext.fg("green")
                print(TREE, end="")
            elif cell == FIRE:
                bext.fg("red")
                print(FIRE, end="")
            elif cell == WATER:
                # NEW: draw the lake as blue water.
                bext.fg("blue")
                print(WATER, end="")
            elif cell == EMPTY:
                print(EMPTY, end="")
        print()

    bext.fg("reset")  # Use the default font color.
    print(f"Grow chance: {GROW_CHANCE * 100:.0f}%  ", end="")
    print(f"Lightning chance: {FIRE_CHANCE * 100:.0f}%  ", end="")
    print("Press Ctrl-C to quit.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
