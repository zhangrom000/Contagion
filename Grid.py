import numpy as N

from Cell import Cell
from Carrier import Carrier
from Traveler import Traveler

class Grid(object):    
    ## Initializing Grid ##
    CITY_PROB = 0.02 #Chance of placing a city
    SUBURBAN_PROB = 0.05 #Chance of placing suburban area
    RURAL_PROB = 0.08 #Chance of placing a rural area
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
        
    def init(self):
        self.GRID = N.empty((self.GRID_WIDTH, self.GRID_HEIGHT), dtype=Cell) #A grid of cells
        self.TRAVELERS = []
        self.TRAVEL_LOC = []
        self.CARRIERS = [] #An array of all the carriers
        self.initGrid()
        #Initialize grid, calls other initializations
        
    def initGrid(self):
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
                            self.addCarrier(x, y, Carrier.NUM_IN_SWARM)  
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
        
    def addCarrier(self, x, y, numSwarm):
        hold = Carrier()
        hold.x = x
        hold.y = y
        hold.NUM_IN_SWARM = numSwarm
        self.CARRIERS.append(hold)
    
    def updateGrid(self):
        dead = 0
        infected = 0
        alive = 0
        recovered = 0
        susceptible = 0
        carriers = 0
        for i in range(len(self.TRAVELERS)):
            self.TRAVELERS[i].move(self)
        for i in range(len(self.CARRIERS)):
            self.CARRIERS[i].update(self)
            carriers += self.CARRIERS[i].NUM_IN_SWARM
            
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
    
    def getCell(self, xy_coords=[]):
        return self.GRID[xy_coords[0]][xy_coords[1]]
    
    def killCarrier(self):
        to_remove = []
        for i in range(len(self.CARRIERS)):
            if (self.CARRIERS[i].NUM_IN_SWARM <= 0):
                to_remove.append(self.CARRIERS[i])
                
        for i in range(len(to_remove)):
            self.CARRIERS.remove(to_remove[i])