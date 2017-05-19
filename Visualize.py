import numpy as np
import matplotlib.pyplot as plt

class Visualize(object):
    
    def plot_env_grid(env_grid):
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
        