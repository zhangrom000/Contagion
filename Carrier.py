
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
    
    def __init__(self, x_init=0, y_init=0, swarm_init = 1, infected="False"):
        self.x = x_init
        self.y = y_init
        self.NUM_IN_SWAM = swarm_init
        self.INFECTED = infected
    
    def update(self):
        self.NUM_IN_SWARM = self.NUM_IN_SWARM * (1 + POP_GROWTH_RATE)
        pass
    
    def Infect(self):
        INFECTED = True
        pass
        
       
