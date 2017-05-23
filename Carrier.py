"""
Carrier contains a Swarm population that will be used in calculating the infection potential.
Swarms will grow exponentially until they reach the max swarm. Once this occurs then the swarm will split off

@author Austen Harp
@version 5/18/2017
Made for use in the Contagion 
"""
import numpy as np

class Carrier(object):
    #### Variables ####
    NUM_IN_SWARM = 10 #Number of carriers in this carrier
    MOBILITY = 0.5 #Ability to travel
    INFECTED = True #Bool
    INFECTION_RATE = 0.9 #Infectious rate, higher rate means more likely to infect.
    LIFESPAN_COUNTER = 10 #Counts the lifespan of the rats.  Becoming infected will cut the lifespan.
    MAX_SWARM_SIZE = 100 #Max number in swarm before the agent splits.
    POP_GROWTH_RATE = 0.1 #Percentage growth rate of this agent. The agent will eventually split.
    x = 1 #x location in grid
    y = 1 #y location in grid
    
    #### Neighbors ####
    NORTH = [x, y + 1]
    EAST = [x + 1, y]
    SOUTH = [x, y - 1]
    WEST =[x - 1, y]
    
    def __init__(self, x_init=0, y_init=0, swarm_init = 1, infected="False", infect_rate=0.2):
        self.x = x_init
        self.y = y_init
        self.NUM_IN_SWAM = swarm_init
        self.INFECTED = infected
        self.INFECTION_RATE = infect_rate
    
    # Update population and location of swarm
    def update(self, env_grid):
        if (self.NUM_IN_SWARM < self.MAX_SWARM_SIZE):
            self.NUM_IN_SWARM = self.NUM_IN_SWARM * (1 + self.POP_GROWTH_RATE)
            
        self.Move(env_grid)
        pass
    
    
    def Move(self, env_grid):
        # Check mobility versus a rng to determine if it moves
        # Check if nearby agents, or for a point of interest
        # move in a direction
        rand = np.random.random()
        
        if (rand > self.MOBILITY):
            possible_moves = []
        
            if (self.NORTH[1] > 0 and 
                env_grid.getCell(self.NORTH).CLEANLINESS >
                env_grid.getCell([self.x, self.y].CLEANLINESS)):
                possible_moves.append(self.NORTH)
            if (self.EAST[0] < env_grid.GRID_WIDTH and 
                env_grid.getCell(self.EAST).CLEANLINESS >
                env_grid.getCell([self.x, self.y].CLEANLINESS)):
                possible_moves.append(self.EAST)
            if (self.SOUTH[1] < env_grid.GRID_HEIGHT and 
                env_grid.getCell(self.SOUTH).CLEANLINESS >
                env_grid.getCell([self.x, self.y].CLEANLINESS)):
                possible_moves.append(self.SOUTH)
            if (self.WEST[0] > 0 and 
                env_grid.getCell(self.WEST).CLEANLINESS >
                env_grid.getCell([self.x, self.y].CLEANLINESS)):
                possible_moves.append(self.WEST)
            
            possible_moves = np.array(possible_moves)
        
            if (np.size(possible_moves) > 0):
                move = possible_moves[np.random.choice(possible_moves.shape[0])]
                self.x = move[0]
                self.y = move[1]
        else:
            pass
        
    def Infect(self):
        INFECTED = True
        pass
        
       
