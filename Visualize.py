import numpy as np
import matplotlib.pyplot as plt
import numpy as N
import matplotlib


"""
Class Visualize

Plots a given grid, which is a 2D array of cells.
Pop cell Filling:        
    100% Healthy = solid green
    100% Infected = solid red
    100% Alive = white
    100% Dead (0 population) = black
    
Cell fades from green to red as population gets infected.
Cell fades to darker color as population dies.
Environment Outlines:
    Suburban: green
    Urban: grey
    Rural: orange
    Land: brown
    
@authors Austen Harp, Garret King, Alex Tang, Roman Zhang
Made for use in the Contagion 
"""
        
class Visualize(object):
        
    
    """
    update_plot
    
    Update the visualization based on the updated data of the simulation
    Also inits the plot if not found
    
    """
    def update_plot(self, gridObj, f = None, axarr = None, wait = True):
        
        height = gridObj.GRID_HEIGHT
        width = gridObj.GRID_WIDTH
        Grid = gridObj.GRID        
        dataEnv = N.zeros((width, height, 3), dtype='f')
        dataPop = N.zeros((width, height, 3), dtype='f')
        dataInf = N.zeros((width, height, 3), dtype='f')
        
        cEmpty = '#8B4513'
        cDead = '#000000'
        # 0 = Land, 1 = City, 2 = Suburban, 3 = Rural, 4 = Barrier
        cEnvMap = [cEmpty, '#808080', 'g', '#FFA500', '#800080']
        # Hex Gradient in 10 steps from green to red
        cInfMap = ['#4BF740', '#5DE13D', '#6FCB3B', '#81B638', '#93A036', \
                        '#A58B33', '#B77531', '#C95F2E', '#DB4A2C', '#FF1F27']
        # Hex Gradient in 10 steps from white to black
        cPopMap = ['#FFFFFF', '#E2E2E2', '#C6C6C6', '#AAAAAA', '#8D8D8D', \
                            '#717171', '#555555', '#383838', '#1C1C1C', cDead]
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
                    if cell.INITIAL_POP == 0: 
                        
                        # grab the hex code belonging to that pop ratio
                        temp = N.array( convert.to_rgb( cEmpty ) ) 
                    else: 
                        popRatio = float(cell.TOTAL_DEAD) / \
                                                        float(cell.INITIAL_POP)
                                                        
                        # convert pop ratio to integer                               
                        popColor = int(popRatio * 9) 
                        
                        # Error check for out of bounds
                        if popColor > 9 or popColor < 0: popColor = 9 
                        
                        # If theres humans left, dont be black
                        if popColor == 9 and cell.INITIAL_POP != \
                        cell.TOTAL_DEAD: popColor = 8 
                        
                        # grab the hex code belonging to that pop ratio
                        temp = N.array( convert.to_rgb( cPopMap[popColor] )) 
                        
                    dataPop[i, j, :] = temp[:] 


                    # Setup the Infected color grid
                    if cell.INITIAL_POP == 0:  # Check if the cell is land
                        temp = N.array( convert.to_rgb( cEmpty ) )                      
                    elif cell.INITIAL_POP == cell.TOTAL_DEAD:#Check if all dead
                        temp = N.array( convert.to_rgb( cDead ) )                       
                    else:
                        infRatio = float(cell.TOTAL_INFECTED + cell.TOTAL_DEAD)\
                        / float(cell.TOTAL_SUSCEPTIBLE + cell.TOTAL_RECOVERED +\
                                        cell.TOTAL_INFECTED + cell.TOTAL_DEAD)
                                        
                        # convert inf ratio to integer
                        infColor = int(infRatio * 9) 
                        
                        # Error check for out of bounds
                        if infColor > 9 or infColor < 0: infColor = 9 
                        
                        # grab the hex code belonging to that inf ratio
                        temp = N.array( convert.to_rgb( cInfMap[infColor] ) ) 

                    dataInf[i, j, :] = temp[:]
                    
        else: # error catch for empty grid
            pass
        
        if f is None:
            #- Create figure and axes objects:        
            f, axarr = plt.subplots(1, 3)  
            
            axarr[0].axis('off')    
            axarr[0].set_title("Environment") 
            axarr[1].axis('off')    
            axarr[1].set_title("Population") 
            axarr[2].axis('off')    
            axarr[2].set_title("Infected")
            
            # Create Legend
            plt.plot([], 'ks', label="City")
            plt.plot([], 'ys', label="Suburban")
            plt.plot([], 'gs', label="Land")        
            plt.plot([], 'ws', label="100% Alive")
            plt.plot([], 'ks', label="100% Dead")
            plt.plot([], 'gs', label="Healthy")
            plt.plot([], 'rs', label="Infected")
            plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.,\
                                                                fontsize = 8)
            
            f.canvas.set_window_title('Contagion')
           
        
        #- Update each grid    
        axarr[0].imshow(dataEnv, interpolation='none',
                extent=[0, width, 0, height],
                zorder=0) 

           
        axarr[1].imshow(dataPop, interpolation='none',
                extent=[0, width, 0, height],
                zorder=0)


        axarr[2].imshow(dataInf, interpolation='none',
                extent=[0, width, 0, height],
                zorder=0)
        
        if wait: plt.pause(0.1)
        plt.show()
        
        return f, axarr
           
    
    """
    plot_agents
    
    Draw all agents on the grid
    """
    def plot_agents(self, gridObj, show=True):
        """
        Carriers are represented as a dot that moves around cells.        
                                        
        Travelers are represented as blue x's
        """
        #takes top_grid and overlay on top of all env_grids
        #takes list_of_carriers and represents them as dots
        #add color to dots
        #update dot movement/merging as they travel through env_grids
        #update dot color fade as carrier data changes
        
        height = gridObj.GRID_HEIGHT
        width = gridObj.GRID_WIDTH
        
        list_of_carriers = gridObj.CARRIERS
        list_of_travelers = gridObj.TRAVELERS
        
        carriers_x = np.zeros(len(list_of_carriers))
        carriers_y = np.zeros(len(list_of_carriers))
        
        travelers_x = np.zeros(len(list_of_travelers))
        travelers_y = np.zeros(len(list_of_travelers))
        
        for i in range(len(list_of_carriers)):
            carriers_x[i] = list_of_carriers[i].x + .5
            carriers_y[i] = width - list_of_carriers[i].y - .5
        
        for j in range(len(list_of_travelers)):
            travelers_x[j] = list_of_travelers[j].x + .5
            travelers_y[j] = width - list_of_travelers[j].y - .5
        
        travelerScatter = plt.scatter(travelers_x, travelers_y, c='b', \
                                                                marker = "x") 
        carrierScatter = plt.scatter(carriers_x, carriers_y, c='y') 
                
        plt.show()
        return carrierScatter, travelerScatter 
