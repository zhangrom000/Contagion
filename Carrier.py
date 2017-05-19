""""
Carrier contains a Swarm population that will be used in calculating the infection potential.
Swarms will grow exponentially until they reach the max swarm. Once this occurs then the swarm will split off

@author Austen Harp
@version 5/18/2017
Made for use in the Contagion 
""""

class Carrier(object):
    #### Variables ####
    NUM_IN_SWARM #Number of carriers in this carrier
    MOBILITY #Ability to travel
    INFECTED #Bool
    INFECTION_RATE #Infectious rate, higher rate means more likely to infect.
    LIFESPAN_COUNTER #Counts the lifespan of the rats.  Becoming infected will cut the lifespan.
    MAX_SWARM_SIZE #Max number in swarm before the agent splits.
    POP_GROWTH_RATE #Percentage growth rate of this agent. The agent will eventually split.
    x # x location in grid
    y # y location in grid
    
    def __init__(self, x_init=0, y_init=0, swarm_init = 1, infected="False", infect_rate=0.2):
        self.x = x_init
        self.y = y_init
        self.NUM_IN_SWAM = swarm_init
        self.INFECTED = infected
        self.INFECTION_RATE = infect_rate
    
    # Update population and location of swarm
    def update(self):
        self.NUM_IN_SWARM = self.NUM_IN_SWARM * (1 + POP_GROWTH_RATE)
        self.Move(self)
        pass
    
    
    def Move(self):
        # Check mobility versus a rng to determine if it moves
        # Check if nearby agents, or for a point of interest
        # move in a direction        
        
    def Infect(self):
        INFECTED = True
        pass
        
       
