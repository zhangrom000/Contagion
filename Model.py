#### Model ####

#Infection will take into acount base probability, number of infected
#rats and humans, population density, pollution level, resource availability,
# and whether the cell is quarantined or not.

import numpy as N
from Grid import Grid
from Visualize import Visualize

TIMELINE = 2 #Time of the model
DT = 1 #Timestep
TIME = (int) (TIMELINE / DT)

G = Grid()
V = Visualize()

dataArr = N.array(TIME) #Array of infection data per timestep
gridArr = N.array(TIME) #Array of grids for each timestep
environArr = N.array(TIME) #Array of enviroment for each timestep

G.init()
for dt in range(TIME):
    G.updateGrid()
    V.plot_all(G)

