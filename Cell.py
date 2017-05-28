import numpy as np
import numpy.random as rand
from Carrier import Carrier
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
    
    def __init__(self, xLoc = 0, yLoc = 0, density = 'Land', lifespan = 14, quarantined = 'False', carrierList = []):
        #### Variables ####
        if (density == 'City'):
            self.ENV_TYPE = 1
            self.INITIAL_POP = 1000
            self.DENSITY = 1
        elif(density == 'Suburban'):
            self.ENV_TYPE = 2
            self.INITIAL_POP = 100
            self.DENSITY = 0.8
        elif(density == 'Rural'):
            self.ENV_TYPE = 3
            self.INITIAL_POP = 10
            self.DENSITY = 0.4
        elif(density == 'Land'):
            self.ENV_TYPE = 0
            self.INITIAL_POP = 0
            self.DENSITY = 0
        else:
            self.INITIAL_POP = 0
            self.DENSITY = 0
            
        self.x = xLoc #X coordinate on the grid
        self.y = yLoc #Y coordinate on the grid
        self.TOTAL_POP = self.INITIAL_POP
        self.AFFLUENCE = rand.random()
        self.POLLUTION = rand.random()
        self.TOTAL_RECOVERED = 0 #Number of infected that have recovered from the contagion
        self.RECOVER_PROBABILITY = 0.05 #Percentage of population recovered after end of lifespan
        self.TOTAL_DEAD = 0#Total Dead Population of cell
        self.TOTAL_INFECTED = 0 #Total Infected Population of cell
        self.LIFESPAN = lifespan #Lifespan (in days) an infected human. 
        self.QUARANTINED = quarantined #Whether or not this cell is blocked off from contagion
        self.INFECTED_ARR = np.zeros(self.LIFESPAN) #Keeps track of the number of infected per time step
        self.carrierList = carrierList
        self.currentTimeStep = 0
        
        self.recovery_days = 7
        

    """
    update_population:
    
    Increment infected count & add result of current time step to infected history
    Num infected increments based on multiple factors:
        Environment type at this Cell's location,
        This cell's Population density type
        This cell's pollution value 
    
    """
    def update_population(self, carriers):
        self.carrierList = carriers
        
        infected = self.infect_rate()
        self.TOTAL_INFECTED = infected
        self.TOTAL_POP -= infected
        
        return self.TOTAL_DEAD, self.TOTAL_INFECTED, self.TOTAL_POP
        
    """
    infect_rate
    
    returns the number of people in this Cell's population to infect in the 
    current time step as a function of polliution, number of infected, and
    affluence.
    
    """    
    def infect_rate(self):
        infect_prob = Carrier.INFECTION_RATE * self.DENSITY
        numToInfect = int((self.carriers_In_Cell() * infect_prob) \
                          + (self.TOTAL_INFECTED * infect_prob))
        return numToInfect
    """
    recover_rate
    
    returns a percentage of infected to recover at the time step that is 
    currently "recovery_days" old 
    
    """     
    def recover_rate(self):
        #pctRecovered = (((10 * self.AFFLUENCE) - (10 * self.POLLUTION))) / 100
        pctRecovered = 0
        return pctRecovered 
    """
    carriers_In_Cell
    
    returns the total of numInSwarm of all Carriers in this cell
    
    PRECONDITION: All carriers contained in self.carrierList are all carriers 
                    whose x-y coordinates are identical to this Cell's x-y 
                    coordinates
    """ 
    def carriers_In_Cell(self):
        totalCarriers = 0
        for c in self.carrierList:
            if (c.x == self.x and c.y == self.y):
                totalCarriers += c.NUM_IN_SWARM
        return totalCarriers