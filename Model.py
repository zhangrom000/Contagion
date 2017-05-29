"""
Class Model

The driver for the Contagion simulation. Contains data relevant to the maintenance
the simulation such as: duration, the grid, metrics, and graphical outputs.
"""
#Infection will take into acount base probability, number of infected
#rats and humans, population density, pollution level, resource availability,
# and whether the cell is quarantined or not.

import numpy as N
import matplotlib.pyplot as plt
from Grid import Grid
from Visualize import Visualize

TIMELINE = 365 * 3 #Timestep duration of the model
DT = 1 #Timestep
TIME = (int) (TIMELINE / DT)
#
G = Grid()
V = Visualize()

dataArr = N.zeros((TIME, 5)) #Array of infection data per timestep
gridArr = list() #Array of grids for each timestep
environArr = N.array(TIME) #Array of enviroment for each timestep

G.init() #Initialize the grid
f, axs = V.init_plot(G)
scat = V.plot_carriers(G, G.CARRIERS)
for dt in range(TIME):
    print dt
    dead, infected, alive, recovered, susceptible = G.updateGrid()
    #print infected
    dataArr[dt][0] = dead
    dataArr[dt][1] = infected
    dataArr[dt][2] = alive
    dataArr[dt][3] = recovered
    dataArr[dt][4] = susceptible
    #gridArr.append(grid)
    scat.remove()
    scat = V.plot_carriers(G, G.CARRIERS)
    V.update_plot(G, f, axs)
    
plt.figure("Stats")
plt.plot(range(TIME), dataArr[:,0], 'k', label="Dead") # dead
plt.plot(range(TIME), dataArr[:,1], 'r', label="Infected") # infected
plt.plot(range(TIME), dataArr[:,2], 'g', label="Alive") # alive
plt.plot(range(TIME), dataArr[:,3], 'b', label="Recovered") # recovered
plt.plot(range(TIME), dataArr[:,4], 'y', label="Susceptible") # susceptible
#plt.title("Percentage of Trees Burned by Probability")
plt.xlabel("Time")
plt.ylabel("Stats")
plt.legend(fontsize=8, loc=1, borderaxespad=0.)
plt.show()
