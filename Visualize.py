import numpy as np
import matplotlib.pyplot as plt
import numpy as N
import matplotlib

class Visualize(object):
    
    def plot_env_grid(): #env_grid, list_of_carriers, show = False):
        
        """
        Plots a given grid, which is a 2D array of cells.
        
        Each cell has a color, each envGrid has an outline color.
        
        Cell Filling:        
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
        
        #take env_grid and give the border an outline
        #loop through each cell in grid and give color based on cell data
        #plot with matplotlib
        #update color hues/shading based on cell data change
    
        width = 15 #env_grid.width
        length = 20 #env_grid.width
        env_grid = np.zeros(shape = (length, width))
        print(env_grid)
        env_grid.fill(2)
        env_grid.astype(int)
        print(env_grid)
    
        data = N.zeros((width, length, 3), dtype='f')
        cmap = ['k', 'b', 'g', '0.5', '0.1']
        convert = matplotlib.colors.ColorConverter()
        
        
        if len(env_grid) != 0:       #- data for a non-empty farm
            #for i in env_grid:
            for i in range(0, width):
                for j in range(0, length):
                    cellVal = int(env_grid[j, i])
                    
                    temp = N.array( convert.to_rgb( cmap[cellVal] ) )
                    data[i, j, :] = temp[:]
                
        else:                              #- data for empty farm
            pass
        
        
        #- Create figure and axes objects:
    
        fig, ax = plt.subplots(1, 1)
    
    
        #- Plot the image, turn off the axes labels, and (maybe) show the plot:    
        ax.imshow(data, interpolation='none',
                extent=[0, width, 0, length],
                zorder=0)
        ax.axis('off')    
        plt.show()
    
    
        #- Return values:    
        return fig, ax
    
        
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
        
    
    plot_env_grid()
