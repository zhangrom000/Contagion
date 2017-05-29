"""
Class Traveler

Represents an agent that moves about the grid. Travelers move between cities.
They may carry infected Carriers around the grid, further infecting areas 
within the grid.
"""
import numpy as np

class Traveler(object):
    
    x = 0
    y = 0
    destination = [0,0]
    speed = 1
    """
    __init__
    
    Initialize this Traveler: x-y coordinate, destination, and rate of movement
    """
    def __init__(self, x_init=0, y_init=0, dest=[0,0], spd=1):
        self.x = x_init
        self.y = y_init
        self.destination = dest
        self.speed = spd
             
    """
    move
    
    update this Traveler's location for the current time step if not 
    currently at the destination
    """
    def move(self, grid):
        #If this Traveler has arrived at its destination, find a new destination
        if self.x == self.destination[0] and self.y == self.destination[1]:
            self.getNewDestination(grid)
        if self.destination[0] > self.x:
            self.x += 1
        if self.destination[0] < self.x:
            self.x -= 1
        if self.destination[1] > self.y:
            self.y += 1
        if self.destination[1] < self.y:
            self.y -= 1
    
    """
    getNewDestination
    
    Determine a new coordinate for this Traveler to travel to
    """
    def getNewDestination(self, grid):
        num = len(grid.TRAVEL_LOC)
        i = 1
        index = range(len(grid.TRAVEL_LOC))
        n = np.random.choice(index, 1)
        dest = grid.TRAVEL_LOC[n]
        while (grid.GRID[dest[0]][dest[1]].INITIAL_POP != 0 or float(grid.GRID[dest[0]][dest[1]].TOTAL_DEAD / (grid.GRID[dest[0]][dest[1]].TOTAL_SUSCEPTIBLE + grid.GRID[dest[0]][dest[1]].TOTAL_RECOVERED + 0.001))) > .5 and i < num:
            n = np.random.choice(index, 1)
            dest = grid.TRAVEL_LOC[n]
            i += 1
        self.destination = dest
