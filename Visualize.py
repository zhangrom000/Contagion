import numpy as np
import matplotlib.pyplot as plt
import numpy as N
import matplotlib
import time as time


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
        
    def init_plot(self, gridObj):
        height = gridObj.GRID_HEIGHT
        width = gridObj.GRID_WIDTH
        Grid = gridObj.GRID        
        dataEnv = N.zeros((width, height, 3), dtype='f')
        dataPop = N.zeros((width, height, 3), dtype='f')
        dataInf = N.zeros((width, height, 3), dtype='f')
        # 0 = Land, 1 = City, 2 = Suburban, 3 = Rural, 4 = Barrier
        cEnvMap = ['#8B4513', '#808080', 'g', '#FFA500', '#800080']
        # Hex Gradient in 10 steps from green to red
        cInfMap = ['#4BF740', '#5DE13D', '#6FCB3B', '#81B638', '#93A036', '#A58B33', '#B77531', '#C95F2E', '#DB4A2C', '#FF1F27']
        # Hex Gradient in 5 steps from white to black
        cPopMap = ['#FFFFFF', '#BFBFBF', '#7F7F7F', '#3F3F3F', '#000000']
        cCarMap = ['#FFFF00'] # Carrier gradient - TODO
        convert = matplotlib.colors.ColorConverter()
        
        # Setup the Environment color grid
        if len(Grid) != 0:
            #for i in env_grid:
            for i in range(0, width):
                for j in range(0, height):
                    # Grab the current cell
                    cell = Grid[j, i]
                           
                    # Setup the Environment color grid
                    temp = N.array( convert.to_rgb( cEnvMap[cell.ENV_TYPE] ) )
                    if len(cell.carrierList) > 0: temp = N.array( convert.to_rgb( cCarMap[0] ) )
                    dataEnv[i, j, :] = temp[:]

                    # Setup the Population color grid
                    if cell.INITIAL_POP == 0: popRatio = 0
                    else: popRatio = cell.TOTAL_DEAD / cell.INITIAL_POP
                    popColor = int(popRatio * 4) # convert pop ratio to integer
                    temp = N.array( convert.to_rgb( cPopMap[popColor] ) ) # grab the hex code belonging to that pop ratio
                    dataPop[i, j, :] = temp[:] 


                    # Setup the Infected color grid
                    if cell.TOTAL_POP == 0: infRatio = 0
                    else: infRatio = cell.TOTAL_INFECTED / cell.TOTAL_POP
                    infColor = int(infRatio * 9) # convert inf ratio to integer
                    temp = N.array( convert.to_rgb( cInfMap[infColor] ) ) # grab the hex code belonging to that inf ratio
                    dataInf[i, j, :] = temp[:]  
                    
        else: # error catch for empty grid
            pass
        
        
        #- Create figure and axes objects:        
        f, axarr = plt.subplots(1, 3)     
    
        #- Plot each grid    
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


        axarr[2].imshow(dataInf, interpolation='none',
                extent=[0, width, 0, height],
                zorder=0)
        axarr[2].axis('off')    
        axarr[2].set_title("Infected Grid") 
        
        plt.ion()
        plt.show()
        
        return f, axarr
        
    
    
    def update_plot(self, gridObj, f, axarr):
        
        height = gridObj.GRID_HEIGHT
        width = gridObj.GRID_WIDTH
        Grid = gridObj.GRID        
        dataEnv = N.zeros((width, height, 3), dtype='f')
        dataPop = N.zeros((width, height, 3), dtype='f')
        dataInf = N.zeros((width, height, 3), dtype='f')
        # 0 = Land, 1 = City, 2 = Suburban, 3 = Rural, 4 = Barrier
        cEnvMap = ['#8B4513', '#808080', 'g', '#FFA500', '#800080']
        # Hex Gradient in 10 steps from green to red
        cInfMap = ['#4BF740', '#5DE13D', '#6FCB3B', '#81B638', '#93A036', '#A58B33', '#B77531', '#C95F2E', '#DB4A2C', '#FF1F27']
        # Hex Gradient in 5 steps from white to black
        cPopMap = ['#FFFFFF', '#BFBFBF', '#7F7F7F', '#3F3F3F', '#000000']
        convert = matplotlib.colors.ColorConverter()
        
        # Setup the Environment color grid
        if len(Grid) != 0:
            #for i in env_grid:
            for i in range(0, width):
                for j in range(0, height):
                    # Grab the current cell
                    cell = Grid[j, i]
                           
                    # Setup the Environment color grid
                    temp = N.array( convert.to_rgb( cEnvMap[cell.ENV_TYPE] ) )
                    dataEnv[i, j, :] = temp[:]

                    # Setup the Population color grid
                    if cell.INITIAL_POP == 0: popRatio = 0
                    else: popRatio = cell.TOTAL_DEAD / cell.INITIAL_POP
                    popColor = int(popRatio * 4) # convert pop ratio to integer
                    if popColor > 4: popColor = 4
                    temp = N.array( convert.to_rgb( cPopMap[popColor] ) ) # grab the hex code belonging to that pop ratio
                    dataPop[i, j, :] = temp[:] 


                    # Setup the Infected color grid
                    if cell.TOTAL_POP == 0: infRatio = 0
                    else: infRatio = cell.TOTAL_INFECTED / cell.TOTAL_POP
                    infColor = int(infRatio * 9) # convert inf ratio to integer
                    if infColor > 9: infColor = 9
                    temp = N.array( convert.to_rgb( cInfMap[infColor] ) ) # grab the hex code belonging to that inf ratio
                    dataInf[i, j, :] = temp[:]  
                    
        else: # error catch for empty grid
            pass
        
        
        #- Plot each grid    
        axarr[0].imshow(dataEnv, interpolation='none',
                extent=[0, width, 0, height],
                zorder=0) 

           
        axarr[1].imshow(dataPop, interpolation='none',
                extent=[0, width, 0, height],
                zorder=0)


        axarr[2].imshow(dataInf, interpolation='none',
                extent=[0, width, 0, height],
                zorder=0)
        
        plt.pause(0.4)
        #f.canvas.draw()
        plt.show()
        
    def plot_carriers(self, gridObj, list_of_carriers=[], show=True):
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
        
        height = gridObj.GRID_HEIGHT
        width = gridObj.GRID_WIDTH
        
        carriers_x = np.zeros(len(list_of_carriers))
        carriers_y = np.zeros(len(list_of_carriers))
        
        for i in range(len(list_of_carriers)):
            carriers_x[i] = list_of_carriers[i].x + 0.5
            carriers_y[i] = width - list_of_carriers[i].y - 0.5
        
        scat = plt.scatter(carriers_x, carriers_y, c='y')        
        plt.show()
        return scat     
