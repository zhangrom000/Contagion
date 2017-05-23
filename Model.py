#### Model ####

#Infection will take into acount base probability, number of infected
#rats and humans, population density, pollution level, resource availability,
# and whether the cell is quarantined or not.

import numpy as N
from Grid import Grid
from Visualize import Visualize

TIMELINE = 3 #Time of the model
DT = 1 #Timestep
TIME = (int) (TIMELINE / DT)
print TIME

G = Grid()
V = Visualize()

dataArr = N.array(TIME) #Array of infection data per timestep
gridArr = list() #Array of grids for each timestep
environArr = N.array(TIME) #Array of enviroment for each timestep

G.init()
for dt in range(TIME):
    grid = G.updateGrid()
    gridArr.append(grid)
    V.plot_all(G)
    V.plot_carriers(G, G.CARRIERS)
