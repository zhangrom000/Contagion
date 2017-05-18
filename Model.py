#### Model ####

#Infection will take into acount base probability, number of infected
#rats and humans, population density, pollution level, resource availability,
# and whether the cell is quarantined or not.

import numpy as N
from Grid import grid
from Visualize import vis

TIMELINE #Time of the model
DT #Timestep
TIME = TIMELINE * DT

dataArr = N.array(TIME) #Array of infection data per timestep
gridArr = N.array(TIME) #Array of grids for each timestep
environArr = N.array(TIME) #Array of enviroment for each timestep

grid.init

for dt in range(TIME):
    dataArr[dt], gridArr[dt], environArr[dt] = grid.update()
    
vis.plotGrid(dataArr, gridArr, environArr)

