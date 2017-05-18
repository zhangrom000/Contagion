import numpy as np
import matplotlib.pyplot as plt

class Visualize(object):
    
    def plot_grid(topGrid, envGrid, list_of_carriers=[]):
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
            
        Carriers are represented as a dot that moves around cells.
                
        Carrier:
            Not Infected: white
            Infected: yellow 
        """
        