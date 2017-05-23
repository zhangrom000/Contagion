import numpy as np
import numpy.random as rand
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
    
    ENV_TYPE = 4
    
    def __init__(self, xLoc = 0, yLoc = 0, density = 'Land', lifespan = 14, quarantined = 'False'):
        #### Variables ####
        if (density == 'City'):
            self.ENV_TYPE = 1
            self.INITIAL_POP = 1000
            self.POLLUTION = 0.9 #The higher the pollution, the faster contagion spread
        elif(density == 'Suburban'):
            self.ENV_TYPE = 2
            self.INITIAL_POP = 100
            self.POLLUTION = 0.5
        elif(density == 'Rural'):
            self.ENV_TYPE = 3
            self.INITIAL_POP = 10
            self.POLLUTION = 0.25
        elif(density == 'Land'):
            self.ENV_TYPE = 0
            self.INITIAL_POP = 0
            self.POLLUTION = 0.0
        else:
            self.INITIAL_POP = 0
            self.POLLUTION = 0.0
        
        self.x = xLoc #X coordinate on the grid
        self.y = yLoc #Y coordinate on the grid
        self.TOTAL_POP = self.INITIAL_POP
        self.CLEANLINESS = self.TOTAL_POP * self.POLLUTION
        
        self.TOTAL_RECOVERED = 0 #Number of infected that have recovered from the contagion
        self.RECOVER_PERCENTAGE = 0.05 #Percentage of population recovered after end of lifespan
        self.TOTAL_DEAD = 0#Total Dead Population of cell
        self.TOTAL_INFECTED = 0 #Total Infected Population of cell
        self.LIFESPAN = lifespan #Lifespan (in days) an infected human. 
        self.QUARANTINED = quarantined #Whether or not this cell is blocked off from contagion
        self.INFECTED_ARR = [] #Keeps track of the number of infected per time step
        self.arrayIterator = 0

    """
    update_population:
    
    Increment infected count & add result of current time step to infected history
    Num infected increments based on multiple factors:
        Environment type at this Cell's location,
        This cell's Population density type
        This cell's pollution value 
    
    """
    def update_population(self, carriersInGrid):
        """
        PSEUDOCODE: 
        Check environment value, agent state at the coordinate of this Cell 
        in order to determine incrementation of infected population within this
        time step. Increment number of dead based on infected lifespan. 
        """
        
        if self.TOTAL_INFECTED == 0:
            for carrier in carriersInGrid:
                if (carrier.x == self.x and carrier.y == self.y):
                    #compare random value between 1 and 0 to infect_probability
                    #if rand val is less than probability, 
                    # TOTAL_INFECTED ++
                    randVal = rand.random()
                    if (randVal < self.infect_probability):
                        self.TOTAL_INFECTED += 1
                    
        elif (self.TOTAL_INFECTED > 0 and self.TOTAL_INFECTED < self.TOTAL_POPULATION):
            randVal = rand.random()
            #generate random value 1-0, 
            #if value < infect_probability, increment numInfected by Arbitrary amt
            if (randVal < self.infect_probability):
                self.TOTAL_INFECTED += 2
        else:
            self.INFECTED_ARR[self.arrayIterator] = self.TOTAL_INFECTED
            self.arrayIterator += 1
    
    def infect_probability(self):
        probability = 0.0
        if  self.TOTAL_POPULATION > 1000:
            probability += 0.5
        elif self.TOTAL_POPULATION < 1000 and self.TOTAL_POPULATION > 100:
            probability += 0.35
        elif self.TOTAL_POPULATION < 100 and self.TOTAL_POPULATION > 10:
            probability += 0.2
        else:
            probability += 0.15
            
        if self.POLLUTION > 0.8:
            probability += 0.2
            
        elif self.POLLUTION > 0.5:
            probability += 0.1
        else: 
            probability += 0.05
            
        return probability