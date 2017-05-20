import numpy as N

#from Cell import cell
#from Carrier import carrier

class Grid(object):
    #### Variables ####
    
    ## Initial Population Variables ##
    CARRIER_POP_INIT = 1 #Inital population of carriers per agent
    
    CITY_POP_INIT = 1 #initial population for a city
    CITY_POP_RANGE = 1 #Range around initial size
    SUBURBAN_POP_INIT = 1 #initial population for a Suburban
    SUBURBAN_POP_RANGE = 1  #Range around initial size
    RURAL_POP_INIT = 1 #initial population for a rural
    RURAL_POP_RANGE = 1 #Range around initial size
    
    ## Initializing Grid ##
    CITY_PROB = 0.02 #Chance of placing a city
    SUBURBAN_PROB = 0.05 #Chance of placing suburban area
    RURAL_PROB = 0.08 #Chance of placing a rural area
    BARRIER_PROB = 0
    
    CARRIER_PROB = 1 #Chance of placing a carrier agent
    CARRIER_RANGE = 1 #Nunber of agents to place
    
    POLLUTION_BASE = 1 #Initialize cell polution level
    POLLUTION_RANGE = 1 #Range of pollution
    
    # Cell Type Values #
    LAND = 0
    CITY = 1
    SUBURBAN = 2
    RURAL = 3
    BARRIER = 4
    
    # Grid Size #
    GRID_WIDTH = 20
    GRID_HEIGHT = 20
    
    ## Transmission Variables ##
    BASE_INFECTION_PROB = 1 #Base probability of infection
    CARRIER_INFECTION_PROB = 1 #Probabily of carrier becoming infected
    INCUBATION = 1 #Incubation period
    LIFESPAN = 1 #Lifespan of infected individual
    RECOVERY_CHANCE = 1 #Chance of individual's recovery
    
    CELL_MAX_CARRIER_POP = 1 #Max number of carrier population before no more will enter
    
    QUARANTINED_MIN = 1 #Number of living needed to maintain Quarantine
    QUARANTINE_MAX = 1 #Number of infected to implement Quarantine
    
    GRID = [] #A grid of cells
    CARRIERS = [] #An array of all the carriers
        
        
    def init(self):
        self.initGrid()
        #Initialize grid, calls other initializations
        
    def initGrid(self):
        #Initialize the grid and cells
        self.GRID = N.zeros((self.GRID_WIDTH, self.GRID_HEIGHT))
        for x in range(self.GRID_WIDTH):
            for y in range(self.GRID_HEIGHT):
                rand = N.random.random(5)
                if rand[0] <= self.CITY_PROB:
                    self.GRID[x][y] = self.CITY
                    #Initialize city cell
                elif rand[1] <= self.SUBURBAN_PROB:
                    self.GRID[x][y] = self.SUBURBAN
                    #Initialize Suburban cell
                elif rand[2] <= self.RURAL_PROB:
                    self.GRID[x][y] = self.RURAL
                    #Initialize Rural cell
                elif rand[3] <= self.BARRIER_PROB:
                    self.GRID[x][y] = self.BARRIER
                else:
                    self.GRID[x][y] = self.LAND
                if rand[5] <= self.CARRIER_PROB:
                    self.addCarrier(x, y)
        print self.GRID
        
    def addCarrier(x, y):
        i = 1 # Create and add carriers to this position
    
    #def updateGrid():
        #Run through each carrier and cell, calling update for each carrier and then cell.
    
from Grid import Grid
from Visualize import Visualize
G = Grid()
G.init()
V = Visualize()
V.plot_env_grid(G)
#G.init()
