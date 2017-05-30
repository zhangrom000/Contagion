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

## Runtime Variables ##

TIMELINE = 1000 #Timestep duration of this simulation
DT = 1 #Timestep
TIME = (int) (TIMELINE / DT)
graph = True
numSims = 30
multipleSims = 0 #0 for one run, 1 for multiple, 2 for full test

########################

## Methods ##
def singleRun(TIME):
    dataArr = N.zeros((TIME, 6)) #Array of infection data per timestep
    G.init() #Initialize the grid
    f, axs = V.update_plot(G)
    carrierScatter,travelerScatter = V.plot_agents(G)
    for dt in range(TIME):
        print dt
        dead, infected, alive, recovered, susceptible, carriers = G.updateGrid()
        dataArr[dt][0] = dead
        dataArr[dt][1] = infected
        dataArr[dt][2] = alive
        dataArr[dt][3] = recovered
        dataArr[dt][4] = susceptible
        dataArr[dt][5] = carriers
        carrierScatter.remove()
        travelerScatter.remove()
        carrierScatter,travelerScatter = V.plot_agents(G)
        V.update_plot(G, f, axs, graph)
        if len(G.CARRIERS) == 0: 
            TIME = dt
            break
        
    plt.figure("Population")
    plt.plot(range(TIME), dataArr[:TIME,0], 'k', label="Dead") # dead
    plt.plot(range(TIME), dataArr[:TIME,1], 'r', label="Infected") # infected
    plt.plot(range(TIME), dataArr[:TIME,2], 'g', label="Alive") # alive
    plt.plot(range(TIME), dataArr[:TIME,3], 'b', label="Recovered") # recovered
    plt.plot(range(TIME), dataArr[:TIME,4], 'y', label="Susceptible") # susceptible
    plt.xlabel("Time (days)")
    plt.ylabel("Population Size")
    plt.legend(fontsize=8, loc=1, borderaxespad=0.)
    plt.show()
    
    plt.figure("Carrier Population")
    plt.plot(range(TIME), dataArr[:TIME,5], label="Carriers") # dead
    plt.xlabel("Time (days)")
    plt.ylabel("Carrier Population Size")
    plt.show()

def multipleRuns(TIME, numSims):
    dataArr = N.zeros((TIME, 6)) #Array of infection data per timestep
    G.init() #Initialize the grid
    for run in range(numSims):
        G.init() #Initialize the grid
        print run
        for dt in range(TIME):
            dead, infected, alive, recovered, susceptible, carriers = G.updateGrid()
            dataArr[dt][0] += dead
            dataArr[dt][1] += infected
            dataArr[dt][2] += alive
            dataArr[dt][3] += recovered
            dataArr[dt][4] += susceptible
            dataArr[dt][5] += carriers
            if len(G.CARRIERS) == 0: 
                dt = TIME
    dataArr = dataArr / numSims
    plt.figure("Average Population Versus Time")
    plt.plot(range(TIME), dataArr[:TIME,0], 'k', label="Dead") # dead
    plt.plot(range(TIME), dataArr[:TIME,1], 'r', label="Infected") # infected
    plt.plot(range(TIME), dataArr[:TIME,2], 'g', label="Alive") # alive
    plt.plot(range(TIME), dataArr[:TIME,3], 'b', label="Recovered") # recovered
    plt.plot(range(TIME), dataArr[:TIME,4], 'y', label="Susceptible") # susceptible
    plt.xlabel("Time (days)")
    plt.ylabel("Population Size")
    plt.legend(fontsize=8, loc=1, borderaxespad=0.)
    plt.show()
    
    plt.figure("Average Carrier Population Versus Time")
    plt.plot(range(TIME), dataArr[:TIME,5], label="Carriers") # dead
    plt.xlabel("Time (days)")
    plt.ylabel("Carrier Population Size")
    plt.show()

def fullTest(TIME, numSims):
    testCase("Base Case", TIME, numSims)
    testCase("Disease 2 Case", TIME, numSims)
    testCase("Disease 3 Case", TIME, numSims)
    testCase("Grid 2 Case", TIME, numSims)
    testCase("Grid 3 Case", TIME, numSims)
    testCase("No Traveler Case", TIME, numSims)
    
def testCase(name, TIME, numSims):
    dataArr = N.zeros((TIME, 6)) #Array of infection data per timestep
    G.init() #Initialize the grid
    for run in range(numSims):
        G.init() #Initialize the grid
        print run
        for dt in range(TIME):
            dead, infected, alive, recovered, susceptible, carriers = G.updateGrid()
            dataArr[dt][0] += dead
            dataArr[dt][1] += infected
            dataArr[dt][2] += alive
            dataArr[dt][3] += recovered
            dataArr[dt][4] += susceptible
            dataArr[dt][5] += carriers
            if len(G.CARRIERS) == 0: 
                dt = TIME
    dataArr = dataArr / numSims
    plt.figure(name + " Average Population Versus Time")
    plt.plot(range(TIME), dataArr[:TIME,0], 'k', label="Dead") # dead
    plt.plot(range(TIME), dataArr[:TIME,1], 'r', label="Infected") # infected
    plt.plot(range(TIME), dataArr[:TIME,2], 'g', label="Alive") # alive
    plt.plot(range(TIME), dataArr[:TIME,3], 'b', label="Recovered") # recovered
    plt.plot(range(TIME), dataArr[:TIME,4], 'y', label="Susceptible") # susceptible
    plt.xlabel("Time (days)")
    plt.ylabel("Population Size")
    plt.legend(fontsize=8, loc=1, borderaxespad=0.)
    plt.show()
    
    plt.figure(Name + "Average Carrier Population Versus Time")
    plt.plot(range(TIME), dataArr[:TIME,5], label="Carriers") # dead
    plt.xlabel("Time (days)")
    plt.ylabel("Carrier Population Size")
    plt.show()

    

######### MAIN #########
G = Grid()
V = Visualize()
if multipleSims == 0:
    singleRun(TIME)
elif multipleSims == 1:
    multipleRuns(TIME, numSims)
elif multipleSims == 2:
    fullTest(TIME, numSims)