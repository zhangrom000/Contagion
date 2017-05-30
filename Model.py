"""
Class Model

The driver for the Contagion simulation. Contains data relevant to the 
maintenance and analysis of the simulation such as: duration, the grid, metrics, 
and graphical outputs.
"""
#Infection will take into acount base probability, number of infected
#rats and humans, population density, pollution level, resource availability,
# and whether the cell is quarantined or not.

import numpy as N
import matplotlib.pyplot as plt
from Grid import Grid
from Visualize import Visualize

## Runtime Variables ##

TIMELINE = 365 * 3 #Timestep duration of this simulation
DT = 1 #Timestep
TIME = (int) (TIMELINE / DT)
graph = True #Play the results in real time for single run
travelers = True
gridType = 0 #0=Base, 1=Low Density, 2=High Density
plagueType = 0 #0=Black Plague, 1=Flu, 2=Modern Plague, 3=Justinian Plague
numSims = 40
multipleSims = 0 #0 for one run, 1 for multiple, 2 for full test

########################

## Methods ##
"""
singleRun

For testing
"""
def singleRun(TIME, travelers, gridType, plagueType):
    dataArr = N.zeros((TIME, 6)) #Array of infection data per timestep
    G.init(travelers, gridType, plagueType) #Initialize the grid
    f, axs = V.update_plot(G)
    carrierScatter,travelerScatter = V.plot_agents(G)
    for dt in range(TIME):
        #print dt
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
    
    # dead
    plt.plot(range(TIME), dataArr[:TIME,0], 'k', label="Dead") 
    
    # infected
    plt.plot(range(TIME), dataArr[:TIME,1], 'r', label="Infected")
    
    # alive
    plt.plot(range(TIME), dataArr[:TIME,2], 'g', label="Alive")
    
    # recovered
    plt.plot(range(TIME), dataArr[:TIME,3], 'b', label="Recovered")
    
    # susceptible
    plt.plot(range(TIME), dataArr[:TIME,4], 'y', label="Susceptible") 
    plt.xlabel("Time (days)")
    plt.ylabel("Population Size")
    plt.legend(fontsize=8, loc=1, borderaxespad=0.)
    plt.show()
    
    plt.figure("Carrier Population")
    plt.plot(range(TIME), dataArr[:TIME,5], label="Carriers") # dead
    plt.xlabel("Time (days)")
    plt.ylabel("Carrier Population Size")
    plt.show()

"""
multipleRuns

For testing
"""
def multipleRuns(TIME, numSims, travelers, gridType, plagueType):
    dataArr = N.zeros((TIME, 6)) #Array of infection data per timestep
    for run in range(numSims):
        G.init(travelers, gridType, plagueType) #Initialize the grid
        print run
        for dt in range(TIME):
            dead, infected, alive, recovered, susceptible, carriers = \
                                                                G.updateGrid()
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
    
    # dead
    plt.plot(range(TIME), dataArr[:TIME,0], 'k', label="Dead") 
    
    # infected
    plt.plot(range(TIME), dataArr[:TIME,1], 'r', label="Infected") 
    
    # alive
    plt.plot(range(TIME), dataArr[:TIME,2], 'g', label="Alive") 
    
    # recovered
    plt.plot(range(TIME), dataArr[:TIME,3], 'b', label="Recovered") 
    
    # susceptible
    plt.plot(range(TIME), dataArr[:TIME,4], 'y', label="Susceptible") 
    plt.xlabel("Time (days)")
    plt.ylabel("Population Size")
    plt.legend(fontsize=8, loc=1, borderaxespad=0.)
    plt.show()
    
    plt.figure("Average Carrier Population Versus Time")
    plt.plot(range(TIME), dataArr[:TIME,5], label="Carriers") # dead
    plt.xlabel("Time (days)")
    plt.ylabel("Carrier Population Size")
    plt.show()

"""
fullTest

For testing
"""
def fullTest(TIME, numSims):
    testCase("Base Case", TIME, numSims, True, 0, 0)
    testCase("Modern Plague Case", TIME, numSims, True, 0, 2)
    testCase("Justinian Plague Case", TIME, numSims, True, 0, 3)
    testCase("Flu Case", TIME, numSims, True, 0, 1)
    testCase("Low Density Grid Case", TIME, numSims, True, 1, 0)
    testCase("High Density Grid Case", TIME, numSims, True, 2, 0)
    testCase("No Traveler Case", TIME, numSims, False, 0, 0)
"""
testCase

For testing 
"""    
def testCase(name, TIME, numSims, travelers, gridType, plagueType):
    dataArr = N.zeros((TIME, 6)) #Array of infection data per timestep
    print name
    for run in range(numSims):
        G.init(travelers, gridType, plagueType) #Initialize the grid
        print run
        for dt in range(TIME):
            #print dt
            dead, infected, alive, recovered, susceptible, carriers = \
                                                                G.updateGrid()
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
    
    # dead
    plt.plot(range(TIME), dataArr[:TIME,0], 'k', label="Dead") 
    
    # infected
    plt.plot(range(TIME), dataArr[:TIME,1], 'r', label="Infected") 
    
    # alive
    plt.plot(range(TIME), dataArr[:TIME,2], 'g', label="Alive") 
    
    # recovered
    plt.plot(range(TIME), dataArr[:TIME,3], 'b', label="Recovered") 
    
    # susceptible
    plt.plot(range(TIME), dataArr[:TIME,4], 'y', label="Susceptible") 
    plt.xlabel("Time (days)")
    plt.ylabel("Population Size")
    plt.legend(fontsize=8, loc=1, borderaxespad=0.)
    plt.show()
    
    plt.figure(name + "Average Carrier Population Versus Time")
    plt.plot(range(TIME), dataArr[:TIME,5], label="Carriers") # dead
    plt.xlabel("Time (days)")
    plt.ylabel("Carrier Population Size")
    plt.show()

    

######### MAIN #########
G = Grid()
V = Visualize()
if multipleSims == 0:
    singleRun(TIME, travelers, gridType, plagueType)
elif multipleSims == 1:
    multipleRuns(TIME, numSims, travelers, gridType, plagueType)
elif multipleSims == 2:
    fullTest(TIME, numSims)