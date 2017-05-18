import numpy as np

class Cell(object):
    
    def __init__(self,xLoc, yLoc, density):
        #### Variables ####
        if (density == 'Urban'):
            self.TOTAL_POP = 1000
            self.POLLUTION = 0.9 
        elif(density == 'Suburban'):
            self.TOTAL_POP = 100
            self.POLLUTION = 0.5
        elif(density == 'Rural'):
            self.TOTAL_POP = 10
            self.POLLUTION = 0.25
        elif(density == 'Land'):
            self.TOTAL_POP = 0
            self.POLLUTION = 0.0
        else:
            self.TOTAL_POP = 0
            self.POLLUTION = 0.0
            
        self.x = xLoc
        self.y = yLoc
        
        self.TOTAL_RECOVERED = 0 #Number of infected that have recovered from the contagion
        self.RECOVER_PERCENTAGE = 0.05 #Percentage of population recovered after end of lifespan
        self.TOTAL_DEAD = 0#Total Dead Population of cell
        self.TOTAL_INFECTED = 0 #Total Infected Population of cell
        self.LIFESPAN = 14 #Lifespan (in days) an infected human. 
        self.QUARANTINED = false #Bool
        self.INFECTED_ARR = [] #Keeps track of the number of infected per time step

    """
    Increment infected count & add result of current time step to infected history
    Num infected increments based on multiple factors:
        Environment type at this Cell's location,
        This cell's Population density type
        This cell's pollution value 
    
    """
    def update_population(self):
        #TODO
    
        