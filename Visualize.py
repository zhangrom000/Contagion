import numpy as np
import matplotlib.pyplot as plt
import numpy as N
import matplotlib


"""
Plots a given grid, which is a 2D array of cells.

Pop cell Filling:        
    100% alive = solid green
    100% infected = solid red
    100% dead (0 population) = black
    
Cell fades from green to red as population gets infected.
Cell fades to darker color as population dies.

Environment Outlines:
    Suburban: green
    Urban: grey
    Rural: orange
    Land: brown
    Barrier: purple
"""
        
class Visualize(object):
        
    def plot_all(self, gridObj, show = True):
        
        # Below is me trying to figure out how to split this method into different functions
        #     So far havent gotten them to work. 
        #envFig, envAx = plt.subplots()  
        #popFig, popAx = self.plot_pop_grid(gridObj, False)
        #envFig, envAx = self.plot_env_grid(gridObj, False)
        #f, axarr = plt.subplots(2)
        #envFig, (envAx, popAx) = plt.subplots(2, sharex=True, sharey=True)        
        #popFig, popAx = plt.subplots()
        
        height = gridObj.GRID_HEIGHT
        width = gridObj.GRID_WIDTH
        Grid = gridObj.GRID        
        dataEnv = N.zeros((width, height, 3), dtype='f')
        dataPop = N.zeros((width, height, 3), dtype='f')
        # 0 = Land, 1 = City, 2 = Suburban, 3 = Rural, 4 = Barrier
        cmap = ['#8B4513', '#808080', 'g', '#FFA500', '#800080']
        # Hex Gradient in 10 steps from green to red
        cPopMap = ['#4BF740', '#5DE13D', '#6FCB3B', '#81B638', '#93A036', '#A58B33', '#B77531', '#C95F2E', '#DB4A2C', '#FF1F27']
        convert = matplotlib.colors.ColorConverter()
        
        
        if len(Grid) != 0:
            #for i in env_grid:
            for i in range(0, width):
                for j in range(0, height):
                    cellVal = int(Grid[j, i])                    
                    temp = N.array( convert.to_rgb( cmap[cellVal] ) )
                    dataEnv[i, j, :] = temp[:]
                
        else: # error catch for empty grid
            pass

        # Setup the Population color grid
        if len(Grid) != 0:
            #for i in env_grid:
            for i in range(0, width):
                for j in range(0, height):
                    cell = Grid[j, i]
                    popRatio = cell.TOTAL_INFECTED / cell.TOTAL_POP
                    popColor = int(popRatio * 9) # convert pop ratio to integer
                    temp = N.array( convert.to_rgb( cPopMap[popColor] ) ) # grab the hex code belonging to that pop ratio
                    dataPop[i, j, :] = temp[:]
                
        else: # error catch for empty grid
            pass
        
        
        #- Create figure and axes objects:        
        f, axarr = plt.subplots(1, 2) 
    
    
        #- Plot the image, turn off the axes labels, and (maybe) show the plot:    
        axarr[0].imshow(dataEnv, interpolation='none',
                extent=[0, width, 0, height],
                zorder=0)
        axarr[0].axis('off')    
        axarr[0].set_title("Environment Grid") 

           
        axarr[1].imshow(dataPop, interpolation='none',
                extent=[0, width, 0, height],
                zorder=0)
        axarr[1].axis('off')    
        axarr[1].set_title("Population Grid") 

        plt.show()
        
    def plot_top_grid(top_grid, list_of_carriers=[]):
        """
        Carriers are represented as a dot that moves around cells.
        Carrier dots grow in size depending on population of swarm.        
                                        
        Carrier:
            Not Infected: white
            Infected: yellow
            
        Dot fades from white to yellow depending on infected amount.
        """
        
        #takes top_grid and overlay on top of all env_grids
        #takes list_of_carriers and represents them as dots
        #add color to dots
        #update dot movement/merging as they travel through env_grids
        #update dot color fade as carrier data changes
        
