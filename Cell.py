
class Cell(object):
    #### Variables ####
    TOTAL_POP #Total Living Population of cell
    TOTAL_DEAD #Total Dead Population of cell
    TOTAL_INFECTED #Total Infected Population of cell
    
    POLLUTION #General level of Hygiene
    RESOURCE_AVAILABILITY #General access to medicine
    
    LIFESPAN #Lifespan of an infected human. Decides the length of the following array.
    INFECTED_ARR[] #Keeps track of the number of infected by day
    
    QUARANTINED #Bool
    