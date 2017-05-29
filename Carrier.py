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
    NUM_IN_SWARM = np.random.randint(1, 6)  #Number of carriers in this carrier
    #MOBILITY = 0.5 #Ability to travel
    INFECTED = True #Bool
    INFECTION_RATE = 0.1 #Infectious rate, higher rate means more likely to infect.
    LIFESPAN = .05 #Percentage of swarm lost each timestep
    MAX_SWARM_SIZE = 100 #Max number in swarm before the agent splits.
    POP_GROWTH_RATE = 0.2 #Percentage growth rate of this agent. The agent will eventually split.
    x = 1 #x location in grid
    y = 1 #y location in grid
    
    #### Neighbors ####
    NORTH = [x, y + 1]
    NORTHEAST = [x + 1, y + 1]
    EAST = [x + 1, y]
    SOUTHEAST = [x + 1, y - 1]
    SOUTH = [x, y - 1]
    SOUTHWEST = [x - 1, y - 1]
    WEST =[x - 1, y]
    NORTHWEST =[x - 1, y + 1]
    
    def __init__(self, x_init=0, y_init=0, swarm_init = 1, infected="False", infect_rate=0.2):
        self.x = x_init
        self.y = y_init
        self.NUM_IN_SWARM = swarm_init
        self.INFECTED = infected
        self.INFECTION_RATE = infect_rate
    
    # Update population and location of swarm
    def update(self, env_grid):
        self.NORTH = [self.x, self.y + 1]
        self.NORTHEAST = [self.x + 1, self.y + 1]
        self.EAST = [self.x + 1, self.y]
        self.SOUTHEAST = [self.x + 1, self.y - 1]
        self.SOUTH = [self.x, self.y - 1]
        self.SOUTHWEST = [self.x - 1, self.y - 1]
        self.WEST =[self.x - 1, self.y]
        self.NORTHWEST =[self.x - 1, self.y + 1]
        
        self.die(env_grid)
        self.grow(env_grid)
        self.split(env_grid)
        self.Move(env_grid)
        pass
    
    
    def Move(self, env_grid):
        # Check mobility versus a rng to determine if it moves
        # Check if nearby agents, or for a point of interest
        # move in a direction        
        possible_moves = []
    
        if (self.NORTH[1] < env_grid.GRID_HEIGHT and
            env_grid.getCell(self.NORTH).TOTAL_SUSCEPTIBLE >=
            env_grid.getCell([self.x, self.y]).TOTAL_SUSCEPTIBLE):
            possible_moves.append(self.NORTH)
        if (self.NORTH[1] < env_grid.GRID_HEIGHT and self.EAST[0] < env_grid.GRID_WIDTH and
            env_grid.getCell(self.NORTHEAST).TOTAL_SUSCEPTIBLE >=
            env_grid.getCell([self.x, self.y]).TOTAL_SUSCEPTIBLE):
            possible_moves.append(self.NORTHEAST)    
        if (self.EAST[0] < env_grid.GRID_WIDTH and 
            env_grid.getCell(self.EAST).TOTAL_SUSCEPTIBLE >=
            env_grid.getCell([self.x, self.y]).TOTAL_SUSCEPTIBLE):
            possible_moves.append(self.EAST)
        if (self.SOUTH[1] >= 0 and self.EAST[0] < env_grid.GRID_WIDTH and
            env_grid.getCell(self.SOUTHEAST).TOTAL_SUSCEPTIBLE >=
            env_grid.getCell([self.x, self.y]).TOTAL_SUSCEPTIBLE):
            possible_moves.append(self.SOUTHEAST)
        if (self.SOUTH[1] >= 0 and 
            env_grid.getCell(self.SOUTH).TOTAL_SUSCEPTIBLE >=
            env_grid.getCell([self.x, self.y]).TOTAL_SUSCEPTIBLE):
            possible_moves.append(self.SOUTH)
        if (self.SOUTH[1] >= 0 and self.WEST[0] >= 0 and
            env_grid.getCell(self.SOUTHWEST).TOTAL_SUSCEPTIBLE >=
            env_grid.getCell([self.x, self.y]).TOTAL_SUSCEPTIBLE):
            possible_moves.append(self.SOUTHWEST)
        if (self.WEST[0] >= 0 and 
            env_grid.getCell(self.WEST).TOTAL_SUSCEPTIBLE >=
            env_grid.getCell([self.x, self.y]).TOTAL_SUSCEPTIBLE):
            possible_moves.append(self.WEST)
        if (self.NORTH[1] < env_grid.GRID_HEIGHT and self.WEST[0] >= 0 and
            env_grid.getCell(self.NORTHWEST).TOTAL_SUSCEPTIBLE >=
            env_grid.getCell([self.x, self.y]).TOTAL_SUSCEPTIBLE):
            possible_moves.append(self.NORTHWEST)
        
        possible_moves = np.array(possible_moves)
        if (env_grid.getCell([self.x, self.y]).TOTAL_SUSCEPTIBLE + env_grid.getCell([self.x, self.y]).TOTAL_RECOVERED) == 0:
            travProb = 1
        else:
            travProb = 0.4
        travelers = []
        if (np.size(possible_moves) > 0):
            for i in env_grid.TRAVELERS:
                for j in possible_moves:
                    if i.x == j[0] and i.y == j[1] and np.random.random() < travProb:
                        travelers.append(i)
            if len(travelers) != 0:
                hold = np.random.choice(travelers)
                self.x = hold.x
                self.y = hold.y
            else:
                move = possible_moves[np.random.choice(possible_moves.shape[0])]
                self.x = move[0]
                self.y = move[1]
    
    def split(self, env_grid):
        if (self.NUM_IN_SWARM >= self.MAX_SWARM_SIZE):
            new_swarm = self.NUM_IN_SWARM / 2
            self.NUM_IN_SWARM -= new_swarm
            env_grid.addCarrier(self.x, self.y, new_swarm)       
    
    def die(self,env_grid):    
        if (env_grid.getCell([self.x, self.y]).ENV_TYPE == 0):
            
            num_dead = self.NUM_IN_SWARM * \
            (self.LIFESPAN) + 1
            
            if (num_dead >= 1):
                self.NUM_IN_SWARM -= num_dead
                
    def grow(self, env_grid):
        if (self.NUM_IN_SWARM < self.MAX_SWARM_SIZE and
            env_grid.getCell([self.x, self.y]).TOTAL_SUSCEPTIBLE > 1):
            
            num_growth = self.NUM_IN_SWARM * self.POP_GROWTH_RATE
            
            if (num_growth >= 1):
                self.NUM_IN_SWARM += num_growth
            elif (self.NUM_IN_SWARM != 0):
                self.NUM_IN_SWARM += 1
                
        
