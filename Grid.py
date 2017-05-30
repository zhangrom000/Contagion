"""
Class Grid

Grid represents the finite cartesian plane which serves as the overall environment
of this agent based model. Cells of populations are defined as a coordinate on 
this Grid. The agents, Carrier objects, are defined as coordinates on this grid. 
The Carrier agents move independently through this Grid using Von Neumann 
neighborhood move policy.
"""
import numpy as N
from Cell import Cell
from Carrier import Carrier
from Traveler import Traveler

class Grid(object):    
    ## Initializing Grid ##
    
    LOW_DENSITY = {'CITY_PROB': 0.005, 'SUBURBAN_PROB': 0.03, 'RURAL_PROB': 0.06}
    BASE = {'CITY_PROB': 0.02, 'SUBURBAN_PROB': 0.05, 'RURAL_PROB': 0.08}
    HIGH_DENSITY = {'CITY_PROB': 0.1, 'SUBURBAN_PROB': 0.1, 'RURAL_PROB': 0.1}
    
    GRID_TYPE = BASE
    
    CITY_PROB = GRID_TYPE['CITY_PROB'] #Chance of placing a city
    SUBURBAN_PROB = GRID_TYPE['SUBURBAN_PROB'] #Chance of placing suburban area
    RURAL_PROB = GRID_TYPE['RURAL_PROB'] #Chance of placing a rural area
    BARRIER_PROB = 0
    
    # Grid Size #
    GRID_WIDTH = 20
    GRID_HEIGHT = 20
    
    GRID = N.empty((GRID_WIDTH, GRID_HEIGHT), dtype=Cell) #A grid of cells
    TRAVELERS = []
    TRAVEL_LOC = []
    MAX_TRAVELERS = 8
    CARRIERS = [] #An array of all the carriers
    MAX_CARRIERS = 8        
        
    """
    init
    
    Initialize the lists of objects contained within this Grid.
    """
    def init(self, travelers=True, plagueType=0, gridType=0):
        self.GRID = N.empty((self.GRID_WIDTH, self.GRID_HEIGHT), dtype=Cell) #A grid of cells
        self.TRAVELERS = []
        self.TRAVEL_LOC = []
        self.CARRIERS = [] #An array of all the carriers
        
        if travelers == True:
            self.MAX_TRAVELERS = 8
        else:
            self.MAX_TRAVELERS = 0
        
        if gridType == 0:
            self.GRID_TYPE = self.BASE
        elif gridType == 1:
            self.GRID_TYPE = self.LOW_DENSITY
        elif gridType == 2:
            self.GRID_TYPE = self.HIGH_DENSITY
        
        self.CITY_PROB = self.GRID_TYPE['CITY_PROB'] #Chance of placing a city
        self.SUBURBAN_PROB = self.GRID_TYPE['SUBURBAN_PROB'] #Chance of placing suburban area
        self.RURAL_PROB = self.GRID_TYPE['RURAL_PROB'] #Chance of placing a rural area
        
        self.initGrid(plagueType)
        #Initialize grid, calls other initializations
        
    """
    initGrid
    
    Initialize this Grid; define the range of the grid, define environment types
    for subsets of the grid at random locations. Probability of an environment
    being rural > suburban > city.
    """
    def initGrid(self, plagueType):
        #Initialize the grid and cells
        for x in range(self.GRID_WIDTH):
            for y in range(self.GRID_HEIGHT):
                rand = N.random.random(5)
                if rand[0] <= self.CITY_PROB:
                    #self.GRID[x][y] = self.CITY
                    self.GRID[x][y]= Cell(x, y, 'City')
                    if len(self.CARRIERS) < self.MAX_CARRIERS:
                        self.TRAVEL_LOC.append([x,y])
                        for i in range(self.MAX_CARRIERS):
                            self.addCarrier(x, y, Carrier.NUM_IN_SWARM, plagueType)  
                    #Initialize city cell
                elif rand[1] <= self.SUBURBAN_PROB:
                    #self.GRID[x][y] = self.SUBURBAN
                    self.GRID[x][y]= Cell(x, y, 'Suburban')
                    self.TRAVEL_LOC.append([x,y])
                    #Initialize Suburban cell
                elif rand[2] <= self.RURAL_PROB:
                    #self.GRID[x][y] = self.RURAL
                    self.GRID[x][y]= Cell(x, y, 'Rural')
                    self.TRAVEL_LOC.append([x,y])
                    #Initialize Rural cell
                elif rand[3] <= self.BARRIER_PROB:
                    #self.GRID[x][y] = self.BARRIER
                    self.GRID[x][y]= Cell(x, y, 'Barrier')
                else:
                    #self.GRID[x][y] = self.LAND
                    self.GRID[x][y]= Cell(x, y, 'Land')
                #if rand[4] <= self.CARRIER_PROB and len(self.CARRIERS) <= self.MAX_CARRIERS:
                    #self.addCarrier(x, y)
        for i in range(self.MAX_TRAVELERS):
            self.TRAVELERS.append(Traveler())
       
    """
    addCarrier
    
    Spawn a Carrier object at a specified x-y coordinate on this Grid
    """ 
    def addCarrier(self, x, y, numSwarm, plagueType):
        self.CARRIERS.append(Carrier(x, y, numSwarm, plagueType))
    
    """
    updateGrid
    
    Return the overall statistics for this Grid: total number of people alive, 
    dead, and infected within every Cell population in this Grid.
    """
    def updateGrid(self):
        dead = 0
        infected = 0
        alive = 0
        recovered = 0
        susceptible = 0
        carriers = 0
        
        #Update travelers in this Grid
        for i in range(len(self.TRAVELERS)):
            self.TRAVELERS[i].move(self)
            
        #Update carriers in this grid
        for i in range(len(self.CARRIERS)):
            self.CARRIERS[i].update(self)
            carriers += self.CARRIERS[i].NUM_IN_SWARM
            
        #Update Cells in this grid
        for i in range(self.GRID_WIDTH):
            for j in range(self.GRID_HEIGHT):
                d, inf, a, r, s = self.GRID[i][j].update_population(self.CARRIERS)
                dead += d
                infected += inf
                alive += a    
                recovered += r
                susceptible += s    
                
        self.killCarrier()
        
        return dead, infected, alive, recovered, susceptible, carriers
    
    """
    getCell
    
    Return the Cell object at a specified x-y coordinate.
    """
    def getCell(self, xy_coords=[]):
        return self.GRID[xy_coords[0]][xy_coords[1]]
    
    """
    killCarrier
    
    Remove a Carrier in the model from the simulation.
    """
    def killCarrier(self):
        to_remove = []
        for i in range(len(self.CARRIERS)):
            if (self.CARRIERS[i].NUM_IN_SWARM < 1):
                to_remove.append(self.CARRIERS[i])
                
        for i in range(len(to_remove)):
            self.CARRIERS.remove(to_remove[i])
