import numpy as np
import random
import numpy.random as rand
from Carrier import Carrier
"""
Class Cell

Represents a population of people and corresponding population density type 
encapsulated in a single X-Y coordinate on the overall grid.
A Cell with a population contains metrics of the population: number of 
total living people in the population, number of infected people, lifespan of 
infected people in this cell, and the history of the population metrics per 
each time step of the simulation

@authors Austen Harp, Garret King, Alex Tang, Roman Zhang
Made for use in the Contagion 
"""
class Cell(object):
    
    ENV_TYPE = 4
    
    """
    __init__
    
    Initialize this Cell: x-y coordinate on grid, environment type, 
    lifespan of population, etc
    """
    def __init__(self, xLoc = 0, yLoc = 0, density = 'Land', plagueType=0, \
                 lifespan = 20, quarantined = 'False', carrierList = []):
        
        if (density == 'City'):
            self.ENV_TYPE = 1
            self.INITIAL_POP = 10000 * random.uniform(0.75, 1.25)
            self.DENSITY = 1
        elif(density == 'Suburban'):
            self.ENV_TYPE = 2
            self.INITIAL_POP = 1000 * random.uniform(0.75, 1.25)
            self.DENSITY = 0.8
        elif(density == 'Rural'):
            self.ENV_TYPE = 3
            self.INITIAL_POP = 100 * random.uniform(0.75, 1.25)
            self.DENSITY = 0.4
        elif(density == 'Land'):
            self.ENV_TYPE = 0
            self.INITIAL_POP = 0
            self.DENSITY = 0
        else:
            self.INITIAL_POP = 0
            self.DENSITY = 0
            
        #Cell uses correct Carrier variables
        self.temp_carrier = Carrier()
        self.temp_carrier.init(Carrier.x, Carrier.y, Carrier.NUM_IN_SWARM, plagueType)
        
        # Percentage of population recovered after end of lifespan
        self.RECOVER_PROBABILITY =  self.temp_carrier.RECOVER_PROBABILITY 
        
        #Lifespan (in days) an infected human.
        self.LIFESPAN =  self.temp_carrier.LIFESPAN_INF  
        
        self.x = xLoc #X coordinate on the grid
        self.y = yLoc #Y coordinate on the grid
        self.TOTAL_SUSCEPTIBLE = self.INITIAL_POP
        self.AFFLUENCE = rand.random()
        self.POLLUTION = rand.random()
        
        #Number of infected that have recovered from the contagion
        self.TOTAL_RECOVERED = 0 
        
        self.TOTAL_DEAD = 0 #Total Dead Population of cell
        self.TOTAL_INFECTED = 0 #Total Infected Population of cell
        
        
        self.QUARANTINED = quarantined 
        
        
        self.INFECTED_ARR = np.zeros(self.LIFESPAN) 
        self.REINFECTION = 45
        self.RECOVERED_ARR = np.zeros(self.REINFECTION)
        
        #Array of Carriers at the same x-y coordinate as this Cell
        self.carrierList = carrierList 
        
        self.currentTimeStep = 0 #The current deltaX of the simulation
        
        """The number of days after which infected people within the population 
        have the chance to recover"""
        self.recovery_days = 7
        

    """
    update_population:
    
    Increment infected count & add result of current time step to infected 
    history.
    Num infected increments based on multiple factors:
        Environment type at this Cell's location,
        This cell's Population density type
        This cell's pollution value 
        This cell's affluence value
    
    """
    def update_population(self, carriers):
        
        #Update the list of carriers for those that might have moved to this Cell
        self.carrierList = carriers 
        self.currentTimeStep += 1
        
        
        ## Reinfect ##
        unrecovered = self.RECOVERED_ARR[self.currentTimeStep %self.REINFECTION]
        self.RECOVERED_ARR[self.currentTimeStep % self.REINFECTION] = 0
        self.TOTAL_RECOVERED -= unrecovered
        self.TOTAL_SUSCEPTIBLE += unrecovered
        
        
        ## Death ##
        if self.INFECTED_ARR[self.currentTimeStep % self.LIFESPAN] > 0:
            recovered = int(self.INFECTED_ARR[self.currentTimeStep % \
                                    self.LIFESPAN] * self.RECOVER_PROBABILITY)
                                    
            self.TOTAL_INFECTED -= self.INFECTED_ARR[self.currentTimeStep % \
                                                                self.LIFESPAN]
            self.TOTAL_RECOVERED += recovered
            
            self.RECOVERED_ARR[self.currentTimeStep % self.REINFECTION] = \
                                                                    recovered
            self.TOTAL_DEAD += self.INFECTED_ARR[self.currentTimeStep % \
                                                    self.LIFESPAN] - recovered
        
        ## Infection ##
        infected = self.infect_rate()
        self.TOTAL_INFECTED += infected
        self.INFECTED_ARR[self.currentTimeStep % self.LIFESPAN] = infected
        self.TOTAL_SUSCEPTIBLE -= infected
        
        return self.TOTAL_DEAD, self.TOTAL_INFECTED, (self.TOTAL_SUSCEPTIBLE +\
            self.TOTAL_INFECTED + self.TOTAL_RECOVERED), self.TOTAL_RECOVERED, \
                                                        self.TOTAL_SUSCEPTIBLE
        
    """
    infect_rate
    
    return the number of people in this Cell's population to infect in the 
    current time step as a function of polliution, number of infected, and
    affluence.
    """    
    def infect_rate(self):
        infect_prob =  self.temp_carrier.INFECTION_RATE * self.DENSITY
        numToInfect = int((self.carriers_In_Cell() * infect_prob) \
                          + (self.TOTAL_INFECTED * infect_prob))
        numToInfect = min(numToInfect, self.TOTAL_SUSCEPTIBLE)
        return numToInfect
    """
    recover_rate
    
    return a percentage of infected to recover at the time step that is 
    currently "recovery_days" old 
    
    """     
    def recover_rate(self):
        #pctRecovered = (((10 * self.AFFLUENCE) - (10 * self.POLLUTION))) / 100
        pctRecovered = 0
        return pctRecovered 
    """
    carriers_In_Cell
    
    return the total of numInSwarm of all Carriers in this cell
    
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
