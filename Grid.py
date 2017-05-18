import numpy as N

from Cell import cell
from Carrier import carrier

class Grid(object):
    #### Variables ####
    
    ## Initial Population Variables ##
    CARRIER_POP_INIT #Inital population of carriers per agent
    
    CITY_POP_INIT #initial population for a city
    CITY_POP_RANGE #Range around initial size
    SUBURBAN_POP_INIT #initial population for a Suburban
    SUBURBAN_POP_RANGE #Range around initial size
    RURAL_POP_INIT #initial population for a rural
    RURAL_POP_RANGE #Range around initial size
    
    
    ## Initializing Grid ##
    CITY_PROB #Chance of placing a city
    SUBURBAN_PROB #Chance of placing suburban area
    RURAL_PROB #Chance of placing a rural area
    
    CARRIER_PROB #Chance of placing a carrier agent
    CARRIER_RANGE #Nunber of agents to place
    
    POLLUTION_BASE #Initialize cell polution level
    POLLUTION_RANGE #Range of pollution
    
    # Cell Type Values #
    LAND = 0
    CITY = 1
    SUBURBAN = 2
    RURAL = 3
    ROAD = 4
    WATER = 5
    
    # Grid Size #
    GRID_WIDTH
    GRID_HEIGHT
    
    ## Transmission Variables ##
    BASE_INFECTION_PROB #Base probability of infection
    CARRIER_INFECTION_PROB #Probabily of carrier becoming infected
    INCUBATION #Incubation period
    LIFESPAN #Lifespan of infected individual
    RECOVERY_CHANCE #Chance of individual's recovery
    
    CELL_MAX_CARRIER_POP #Max number of carrier population before no more will enter
    
    QUARANTINED_MIN #Number of living needed to maintain Quarantine
    QUARANTINE_MAX #Number of infected to implement Quarantine
    
    GRID #A grid of cells
    CARRIERS #An array of all the carriers
    
    def init():
        #Initialize grid, calls other initializations
        
    def initGrid():
        #Initialize the grid and cells
        
    def initCarrier():
        #Initialize the carriers in the grid
        
    def updateGrid():
        #Run through each carrier and cell, calling update for each carrier and then cell.
    