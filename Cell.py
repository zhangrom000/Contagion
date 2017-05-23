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
    
    def __init__(self, xLoc = 0, yLoc = 0, density = 'Land', lifespan = 14, quarantined = 'False', carrierList = []):
        #### Variables ####
        if (density == 'City'):
            self.ENV_TYPE = 1
            self.INITIAL_POP = 1000
        elif(density == 'Suburban'):
            self.ENV_TYPE = 2
            self.INITIAL_POP = 100
            
        elif(density == 'Rural'):
            self.ENV_TYPE = 3
            self.INITIAL_POP = 10
            
        elif(density == 'Land'):
            self.ENV_TYPE = 0
            self.INITIAL_POP = 0
            
        else:
            self.INITIAL_POP = 0
            
            
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
    def update_population(self):
        """
        PSEUDOCODE: 
        Check environment value, agent state at the coordinate of this Cell 
        in order to determine incrementation of infected population within this
        time step. Increment number of dead based on infected lifespan. 
        """
        
        if (self.TOTAL_POP >= self.TOTAL_RECOVERED):
            if (self.TOTAL_INFECTED == 0):
                for carrier in self.carrierList:
                    if (carrier.x == self.x and carrier.y == self.y):
                        #compare random value between 1 and 0 to infect_probability
                        #if rand val is less than probability, 
                        # TOTAL_INFECTED ++
                        randVal = rand.random()
                        if (randVal < self.infect_probability()):
                            self.TOTAL_INFECTED += 1
                        
            elif (self.TOTAL_INFECTED > 0 and self.TOTAL_INFECTED < self.TOTAL_POP):
                #Infect current population based on infect_rate
                self.TOTAL_INFECTED += self.infect_rate()    
            
            numRecovered = 0
            if (self.currentTimeStep >= self.recovery_days):
                randVal = rand.random()
                if (randVal < self.RECOVER_PROBABILITY):
                    numRecovered = int(self.infectedArr[(self.currentTimeStep % self.LIFESPAN) - self.recovery_days] * self.recover_rate)
                    self.TOTAL_RECOVERED += numRecovered
                    self.TOTAL_INFECTED -= numRecovered
                    
            if (self.currentTimeStep >= self.LIFESPAN):
                numDead = int(self.infectedArr[(self.currentTimeStep % self.LIFESPAN) - self.LIFESPAN] - numRecovered)
                self.TOTAL_DEAD += numDead
                self.TOTAL_INFECTED -= numDead
                self.TOTAL_POP -= numDead
                
                
            self.INFECTED_ARR[(self.currentTimeStep % self.LIFESPAN)] = self.TOTAL_INFECTED
            self.currentTimeStep += 1
        else:
            self.quarantined = 'true'
    """
    infect_probability
    
    returns the probability that a population will initially be infected as a
    function of the current population, pollution level, and number of carriers
    currently in this cell.
    
    PRECONDITION: This Cell's population has 0 infected
    
    """
    def infect_probability(self):
        probability = 0.0
        if  self.TOTAL_POP > 1000:
            probability += 0.5
        elif self.TOTAL_POP < 1000 and self.TOTAL_POP > 100:
            probability += 0.35
        elif self.TOTAL_POP < 100 and self.TOTAL_POP > 10:
            probability += 0.2
        else:
            probability += 0.15
            
        if self.POLLUTION > 0.8:
            probability += 0.2
            
        elif self.POLLUTION > 0.5:
            probability += 0.1
        else: 
            probability += 0.05
            
        if (self.carriers_In_cell > 100):
            probability *= 1.25
        else:
            probability *= 1.1
        
        return probability
        
    """
    infect_rate
    
    returns the number of people in this Cell's population to infect in the 
    current time step as a function of polliution, number of infected, and
    affluence.
    
    """    
    def infect_rate(self):
        numToInfect = int((self.POLLUTION * 100) * (self.TOTAL_INFECTED) / self.affluence * 100)
        return numToInfect
    """
    recover_rate
    
    returns a percentage of infected to recover at the time step that is 
    currently "recovery_days" old 
    
    """     
    def recover_rate(self):
        pctRecovered = ((10 * self.affluence) * (10 * self.POLLUTION)) / 100
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
            totalCarriers += c.NUM_IN_SWARM
        return totalCarriers