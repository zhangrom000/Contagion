import numpy as np
"""
Class Cell

Represents a population of people and corresponding population density type 
encapsulated in a single X-Y coordinate on the overall grid.
A Cell with a population contains metrics of the population such as number of 
total living population, number of infected people, lifespan of infected people 
in this cell, and the history of the population metrics per each time step of
the simulation.
"""
class Cell(object):
    
    def __init__(self,xLoc, yLoc, density):
        #### Variables ####
        if (density == 'Urban'):
            self.TOTAL_POP = 1000
            self.POLLUTION = 0.9 #The higher the pollution, the faster contagion spread
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
            
        self.x = xLoc #X coordinate on the grid
        self.y = yLoc #Y coordinate on the grid
        
        self.TOTAL_RECOVERED = 0 #Number of infected that have recovered from the contagion
        self.RECOVER_PERCENTAGE = 0.05 #Percentage of population recovered after end of lifespan
        self.TOTAL_DEAD = 0#Total Dead Population of cell
        self.TOTAL_INFECTED = 0 #Total Infected Population of cell
        self.LIFESPAN = 14 #Lifespan (in days) an infected human. 
        self.QUARANTINED = false #Whether or not this cell is blocked off from contagion
        self.INFECTED_ARR = [] #Keeps track of the number of infected per time step

    """
    update_population:
    
    Increment infected count & add result of current time step to infected history
    Num infected increments based on multiple factors:
        Environment type at this Cell's location,
        This cell's Population density type
        This cell's pollution value 
    
    """
    def update_population(self):
        #TODO
    
    
        